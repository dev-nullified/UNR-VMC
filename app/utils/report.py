from app import db
from app.models.person import Person, PersonSchema
from sqlalchemy.orm import Load
# from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy.ext.serializer import loads, dumps
import json
from marshmallow.fields import Field, String, Integer, Boolean
import marshmallow
from sqlalchemy import or_, and_, not_

class ReportRunner:

    def run_report(self, rules):
        """

        :param fields: Expects a list of strings
        :param conditions: expects a dictionary
        :param params: ??? Not used
        :return: output of query
        """

        # Test conditions
        conditions = {
           1: {
                'attribute' : 'age',
                'operator' : 'le',
                'value' : 95,
            }

        }


        # Step 1 - Get Query Session and model obj
        # query = Person()
        query = self.__get_query_session__(model=Person)
        # print(query)
        model_schema = self.__get__model_schema__(model=Person)

        # Step 2 - add conditions / filter
        # https://stackoverflow.com/questions/7604967/sqlalchemy-build-query-filter-dynamically-from-dict
        # another potential solution https://stackoverflow.com/questions/14845196/dynamically-constructing-filters-in-sqlalchemy
        # another potential solution https://stackoverflow.com/questions/41305129/sqlalchemy-dynamic-filtering
        # if conditions:
        #     for conditionID, condition in conditions.items():
        #         attribute = condition['attribute']
        #         operator = condition['operator']
        #         value = condition['value']
        #         print('Attribute: ' + attribute)
        #         # print('Operator: ' + type(oper))
        #         print('Value: ' + str(value))
        #         # q = q.filter(getattr(Person, attribute).like("%%%s%%" % value))
                
        #         # q = q.filter(getattr(Person, attribute) >= value)
        rules = self.start_recurse_rules(rules)
        query = query.filter(rules)
        print("RULES")
        print(rules)
        print('\n')
        query.filter(rules)

        # Step 3 - Get only the columns we're looking for
        # q.options(load_only(fields))

        # Step 4 - Return the serialized output of the query
        # serialized = dumps(data)
        serialized_result = self.__serialize_query_result__(queryObj=query, modelSchema=model_schema)
        return serialized_result




    
    def __get_query_session__(self, model):    
        """Creates a SQLAlchemy Query session from a provided model
        
        Arguments:
            model {String} -- The name of the model in SQL Alchemy
        
        Returns:
            SQLAlchemy Query -- [description]
        """
        query_session = db.session.query(model)

        return query_session


    def __get__model_schema__(self, model):
        return PersonSchema()

    def __serialize_query_result__(self, queryObj, modelSchema):

        query_result = queryObj.all()

        serialized_data = modelSchema.dumps(query_result, many=True)
        print(serialized_data)
        

        return serialized_data






    def store_report(self):
        pass

    def check_column_valid(self):
        pass

    def check_condition_valid(self):
        pass

    def update_last_run_date(self):
        pass




    # Get report from DB
    def __get_report_by_id__(self):
        pass

    def __set_report_in_db__(self):
        pass

    def __edit_report_in_db__(self):
        pass

    def __build_query_filter__(self, model_class, filter_condition):
        '''
        Return filtered queryset based on condition.
        :param query: takes query
        :param filter_condition: Its a list, ie: [(key,operator,value)]
        operator list:
            lt for < (less than)
            le for <= (less than or equal to)
            eq for == (equal to)
            ne for != (not equal to)
            gt for > (greater than)
            ge for >= (greater than or equal to)


            eq for == (equal to)
            lt for < (less than)

            or for | (logical or)
            and for and (logical and)
            

            in for in_
            like for like
            value could be list or a string
        :return: queryset

        '''

        # if query is None:
        #     query = self.get_query()
        # model_class = query.get()  # returns the query's Model
        model_class = Person

        for raw in filter_condition:

            try:
                key, op, value = raw
                print("key: " + key)
                print("op: " + op)
                print("value: " + str(value))
            except ValueError:
                raise Exception('Invalid filter: %s' % raw)

            column = getattr(Person, key)

            if not column:
                raise Exception('Invalid filter column: %s' % key)

            if op == 'in':

                if isinstance(value, list):
                    filt = column.in_(value)
                else:
                    filt = column.in_(value.split(','))

            if 'not_' in op:
                newOp = op.split('_')[1]

                try:
                    # Check the list of python operators by name, return the first entry found
                    base_attr = list(filter(
                        lambda e: hasattr(column, e % newOp),
                        ['%s', '%s_', '__%s__']
                    ))[0] % newOp

                    attr = not_(base_attr)

                except IndexError:

                    raise Exception('Invalid NOT filter operator: %s' % op)


            else:

                try:
                    # Check the list of python operators by name, return the first entry found
                    attr = list(filter(
                        lambda e: hasattr(column, e % op),
                        ['%s', '%s_', '__%s__']
                    ))[0] % op

                except IndexError:

                    raise Exception('Invalid filter operator: %s' % op)

            if value == 'null':
                value = None

                
        filt = getattr(column, attr)(value)
        print(filter)

        return filt


    def get_query_filter_for_web(self, model):

        # int operations
        # intOps = ['>', '>=', '=', '!=', '<=', '<']
        # stringOps = ['starts with', 'contains', 'ends with', 'is', 'is not']
        boolOps = ['yes', 'no']

        # intOps = ['greater', 'greater_or_equal', 'equal', 'not_equal', 'less', 'less_or_equal']
        intOps = ['gt', 'ge', 'eq', 'neq', 'lt', 'le']

        # stringOps = ['begins_with', 'not_begins_with', 'contains', 'not_contains', 'ends_with', 'not_ends_with']
        # stringOps = ['startswith_op', 'notstartswith_op', 'contains_op', 'notcontains_op', 'endswith_op', 'notendswith_op']
        stringOps = ['startswith', 'not_startswith', 'contains', 'not_contains', 'endswith', 'not_endswith']

        model_schema = self.__get__model_schema__(model=Person)

        # print(model_schema)

        model_schema_fields = model_schema._declared_fields

        filters = []

        for field in model_schema_fields:

            fieldType = model_schema_fields[field]

            id = str # name of the field in the DB
            label = str # display label of the field 
            dataType = str # What is the type of data (string, bool, int)
            inputType = 'text' # How will the data be inputed (Type of input used. Available types are text, number, textarea, radio, checkbox and select)
            values = [] # List of values (required when inputType is radio, checkbox, or select)
            operators = [] # Operators for the db


            # If it is an int
            if isinstance(fieldType, marshmallow.fields.Integer):
                
                id = field
                label = id.capitalize()
                dataType = 'integer'
                inputType = 'number'
                values = None
                operators = intOps

            elif isinstance(fieldType, marshmallow.fields.String):
                id = field
                label = id.capitalize()
                dataType = 'string'
                inputType = 'text'
                values = None
                operators = stringOps

            elif isinstance(fieldType, marshmallow.fields.Boolean):
                id = field
                label = id.capitalize()
                dataType = 'boolean'
                inputType = 'radio'
                values = boolOps
                operators = ['is']

            else:
                id = field
                label = id.capitalize() + 'NOT FOUND'
                dataType = 'string'
                inputType = 'text'
                values = None
                operators = stringOps

            # Create filter rule and append it to the dictionary
            filters.append(
                self.__create_single_selector_for_web_query_builder__(
                    id=id,
                    label=label,
                    dataType=dataType,
                    inputType=inputType,
                    values=values,
                    operators=operators
                )
            )


        # # model_schema.model_schema_field


        # print('\n')
        # print(model_schema_fields)
        # print('\n')

        # for item in model_schema_fields:

        #     # print(type(model_schema.get_instance(data=item)))
        #     print(model_schema_fields[item])
        #     print(type(model_schema_fields[item]))

        # print('\n')
        # print('\n')

        return filters


    def __create_single_selector_for_web_query_builder__(self, id, label, dataType='string', inputType=None, values=None, operators=None):

        newFilter = {
            'id': id,
            'label': label,
            'type': dataType
        }

        if inputType:
            newFilter['input'] = inputType

        if values:
            newFilter['values'] = values

        if operators:
            newFilter['operators'] = operators

        return newFilter
        


    def __parse_rules_from_web__(self, rules_dict):

        filter = []

        if 'condition' in rules_dict:
            if "or" in rules_dict['condition'].lower():
                print("\n OR COND \n")
                print(rules_dict)
                rule = self.__parse_rules_from_web__(rules_dict['rules'])
                return or_(*rule)
            else:
                print("\n AND COND \n")
                print(rules_dict)
                rule = self.__parse_rules_from_web__(rules_dict['rules'])
                return and_(*rule)
                    
        else:
            if isinstance(rules_dict, list):
                for rule in rules_dict:
                    retult = self.__parse_rules_from_web__(rule)
                    # print(retult[0])

                    filter.append(retult) 


            else:
                print(rules_dict)
                id = rules_dict['id']
                operator = rules_dict['operator']
                value = rules_dict['value']
                                
                filt = self.__build_query_filter__(Person, [(id, operator, value)])
                print('RAN ELSE')
                return filt

            # else:
            #     for rule in rules_dict:
            #         print(type(rule))
            #         print(rule)
            #         id = rule['id']
            #         operator = rule['operator']
            #         value = rule['value']
                            
            #         filtr = self.__build_query_filter__(Person, [(id, operator, value)])
            #         filter.append(filtr)

        return filter

    def start_recurse_rules(self, rules_dict):

        valid = rules_dict['valid']

        condition = rules_dict['condition']

        rules = []

        for rule in rules_dict['rules']:

            obj = self.__parse_rules_from_web__(rule)

            if isinstance(obj, list):
                print("LIST FOUND")
                print(obj)

            rules.append(obj)

        if "or" in condition:
            return or_(*rules)
        else:
            # print("\n AND COND \n")
            # print(item)
            return and_(*rules)
        

        # return rules

    # def dummy_run_report(self, rule):
