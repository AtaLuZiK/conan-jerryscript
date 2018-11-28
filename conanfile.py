from conans import ConanFile, CMake, tools


class JerryscriptConan(ConanFile):
    name = "jerryscript"
    version = "1.0-a0a6eaa"
    license = "MIT"
    author = "k000 AtaLuZiK@gmail.com"
    url = "https://github.com/AtaLuZiK/conan-jerryscript"
    description = "Ultra-lightweight JavaScript engine for the Internet of Things."
    topics = ("Javascript", "Javascript egnine")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "debugger": [True, False],
        "error_messages": [True, False],
        "external_context": [True, False],
        "line_info": [True, False],
        "logging": [True, False],
        "mem_stats": [True, False],
        "mem_stress_test": [True, False],
        "profile": ["es5.1", "es2015-subset", "minimal"],
        "regexp_strict_mode": [True, False],
        "regexp_dump": [True, False],
        "snapshot_exec": [True, False],
        "snapshot_save": [True, False],
    }
    default_options = (
        "debugger=False",
        "error_messages=False",
        "external_context=False",
        "line_info=False",
        "logging=False",
        "mem_stats=False",
        "mem_stress_test=False",
        "profile=es5.1",
        "regexp_strict_mode=False",
        "regexp_dump=False",
        "snapshot_exec=False",
        "snapshot_save=False",
    )
    exports_sources = "JerryScript-config.cmake"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        self.run("git clone https://github.com/jerryscript-project/jerryscript.git")
        self.run("cd jerryscript && git checkout a0a6eaaee8af3c684a4065e7b06e2aa45ddfc29d")
        tools.replace_in_file("jerryscript/CMakeLists.txt", "project (Jerry C)",
                              '''project (Jerry C)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["FEATURE_DEBUGGER"] = "ON" if self.options.debugger else "OFF"
        cmake.definitions["FEATURE_ERROR_MESSAGES"] = "ON" if self.options.error_messages else "OFF"
        cmake.definitions["FEATURE_EXTERNAL_CONTEXT"] = "ON" if self.options.external_context else "OFF"
        cmake.definitions["FEATURE_LINE_INFO"] = "ON" if self.options.line_info else "OFF"
        cmake.definitions["FEATURE_LOGGING"] = "ON" if self.options.logging else "OFF"
        cmake.definitions["FEATURE_MEM_STATS"] = "ON" if self.options.mem_stats else "OFF"
        cmake.definitions["FEATURE_MEM_STRESS_TEST"] = "ON" if self.options.mem_stress_test else "OFF"
        cmake.definitions["FEATURE_PROFILE"] = self.options.profile
        cmake.definitions["FEATURE_REGEXP_STRICT_MODE"] = "ON" if self.options.regexp_strict_mode else "OFF"
        cmake.definitions["FEATURE_REGEXP_DUMP"] = "ON" if self.options.regexp_dump else "OFF"
        cmake.definitions["FEATURE_SNAPSHOT_EXEC"] = "ON" if self.options.snapshot_exec else "OFF"
        cmake.definitions["FEATURE_SNAPSHOT_SAVE"] = "ON" if self.options.snapshot_save else "OFF"
        cmake.configure(source_folder=self.name)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="jerryscript/jerry-core/include")
        self.copy("*.h", dst="include", src="jerryscript/jerry-ext/include")
        self.copy("*.h", dst="include", src="jerryscript/jerry-port/default/include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("jerry*", dst="bin", src="bin", keep_path=False)
        self.copy("jerryscript-config.cmake", "cmake", ".")

    def package_info(self):
        self.cpp_info.libs = [
            "jerry-core",
            "jerry-ext",
            "jerry-port-default",
            "jerry-port-default-minimal",
        ]

