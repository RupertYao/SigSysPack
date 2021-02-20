set_toolchains("msvc")

local PY_INCLUDE_PATH = "D:\\Anaconda3\\include"
local PY_LIB_PATH = "D:\\Anaconda3\\libs"
local PYBIND11_INCLUDE_PATH = "D:\\pybind11-2.6.1\\include"
local EIGEN3_PATH = "D:\\Eigen3\\include\\eigen3"

target("Conv_pack")

    -- set kind
    set_kind("shared")

    -- add files
    add_files("./Conv_cpp/Conv/**.cpp")

    add_includedirs(PYBIND11_INCLUDE_PATH,
                    PY_INCLUDE_PATH
                    )
    add_linkdirs(PY_LIB_PATH)
    add_links("python3", "python38")

    set_optimize("faster")
    add_rules("mode.release")

    set_filename("Conv_pack.pyd")
    set_installdir("./install")

target("FFT_pack")

    -- set kind
    set_kind("shared")

    -- add files
    add_files("./FFT_cpp/FFT/**.cpp")

    add_includedirs(PYBIND11_INCLUDE_PATH,
                    PY_INCLUDE_PATH)
    add_linkdirs(PY_LIB_PATH)
    add_links("python3", "python38")

    set_optimize("faster")
    add_rules("mode.release")

    set_filename("FFT_pack.pyd")
    set_installdir("./install")

target("FT_pack")

    -- set kind
    set_kind("shared")

    -- add files
    add_files("./FT_cpp/FourierTransform/**.cpp")

    add_includedirs(EIGEN3_PATH,
                    PYBIND11_INCLUDE_PATH,
                    PY_INCLUDE_PATH
                    )
    add_linkdirs(PY_LIB_PATH)
    add_links("python3", "python38")

    set_optimize("faster")
    add_rules("mode.release")

    set_filename("FT_pack.pyd")
    set_installdir("./install")

--
-- If you want to known more usage about xmake, please see https://xmake.io
--
-- ## FAQ
--
-- You can enter the project directory firstly before building project.
--
--   $ cd projectdir
--
-- 1. How to build project?
--
--   $ xmake
--
-- 2. How to configure project?
--
--   $ xmake f -p [macosx|linux|iphoneos ..] -a [x86_64|i386|arm64 ..] -m [debug|release]
--
-- 3. Where is the build output directory?
--
--   The default output directory is `./build` and you can configure the output directory.
--
--   $ xmake f -o outputdir
--   $ xmake
--
-- 4. How to run and debug target after building project?
--
--   $ xmake run [targetname]
--   $ xmake run -d [targetname]
--
-- 5. How to install target to the system directory or other output directory?
--
--   $ xmake install
--   $ xmake install -o installdir
--
-- 6. Add some frequently-used compilation flags in xmake.lua
--
-- @code
--    -- add debug and release modes
--    add_rules("mode.debug", "mode.release")
--
--    -- add macro defination
--    add_defines("NDEBUG", "_GNU_SOURCE=1")
--
--    -- set warning all as error
--    set_warnings("all", "error")
--
--    -- set language: c99, c++11
--    set_languages("c99", "c++11")
--
--    -- set optimization: none, faster, fastest, smallest
--    set_optimize("fastest")
--
--    -- add include search directories
--    add_includedirs("/usr/include", "/usr/local/include")
--
--    -- add link libraries and search directories
--    add_links("tbox")
--    add_linkdirs("/usr/local/lib", "/usr/lib")
--
--    -- add system link libraries
--    add_syslinks("z", "pthread")
--
--    -- add compilation and link flags
--    add_cxflags("-stdnolib", "-fno-strict-aliasing")
--    add_ldflags("-L/usr/local/lib", "-lpthread", {force = true})
--
-- @endcode
--

