import copy
import platform

from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    
    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["jerryscript:profile"] = "es2015-subset"
        extend_settings.append(settings)
    builder.items.extend(extend_settings)
    
    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["jerryscript:error_messages"] = True
        extend_settings.append(settings)
    builder.items.extend(extend_settings)
    
    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["jerryscript:line_info"] = True
        extend_settings.append(settings)
    builder.items.extend(extend_settings)
    
    extend_settings = []
    for settings in builder.items:
        settings = copy.deepcopy(settings)
        settings.options["jerryscript:logging"] = True
        extend_settings.append(settings)
    builder.items.extend(extend_settings)

    builder.run()
