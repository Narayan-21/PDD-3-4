import configparser

with open('prod.ini', 'w') as prod, open('dev.ini', 'w') as dev:
    prod.write('[Database]\n')
    prod.write('db_host=prod.mynetwork.com\n')
    prod.write('db_name=my_database\n')
    prod.write('\n[Server]\n')
    prod.write('port=8080\n')

    dev.write('[Database]\n')
    dev.write('db_host=dev.mynetwork.com\n')
    dev.write('db_name=my_database\n')
    dev.write('\n[Server]\n')
    dev.write('port=3000\n')

class Section:
    def __init__(self, name, item_dict):
        """
        name: str
            name of section
        item_dict: dict
            dictionary of named (key) config values (value)
        """
        self.name = name
        for key, value in item_dict.items():
            setattr(self, key, value)

class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            section = Section(section_name, config[section_name])
            setattr(self, section_name.casefold(), section)

class SectionType(type):
    def __new__(cls, name, bases, cls_dict, section_name, items_dict):
        cls_dict['__doc__'] = f'Configs for {section_name} section'
        cls_dict['section_name'] = section_name
        for key, value in items_dict.items():
            cls_dict[key] = value
        return super().__new__(cls, name, bases, cls_dict)
class DatabaseSection(metaclass = SectionType, section_name='database', items_dict={'db_host':'db host', 'db_name': 'db name'}):
    pass

class ConfigType(type):
    def __new__(cls, name, bases, cls_dict, env):
        """
        env: str
            The environment we are loading for the config (e.g. prod, dev)
        """
        cls_dict['__doc__'] = f'Config for {env}'
        cls_dict['env'] = env
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            class_name = section_name.capitalize()
            class_attribute_name = section_name.casefold()
            section_items = config[section_name]
            bases = (object, )
            section_cls_dict = {}
            Section = SectionType(
                class_name, bases, section_cls_dict, section_name=section_name, items_dict=section_items
                )
            cls_dict[class_attribute_name] = Section
        return super().__new__(cls, name, bases, cls_dict)

class DevConfig(metaclass=ConfigType, env='dev'):
    pass

class ProdConfig(metaclass=ConfigType, env='prod'):
    pass

print(DevConfig.database.db_name)
print(help(DevConfig))
print(help(DevConfig.database))
