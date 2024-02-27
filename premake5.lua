-- premake5.lua
workspace("Applicaion")

configurations({ "Debug", "Release" })
architecture("x86_64")
cppdialect("C++latest")

project("Application")

kind("ConsoleApp")
language("C++")
cppdialect("C++latest")
targetdir("bin/%{cfg.buildcfg}")

files({ "src/*.h", "src/*.cpp" })

--link locally installed libraries
includedirs({ "dependencies/" .. os.target() .. "/include" })
libdirs({ "dependencies/" .. os.target() .. "/lib" })

if os.target() == "windows" then
	print("windows")
	defines({ "_WIN32", "WIN32", "WINDOWS" })
elseif os.target() == "linux" then
	print("linux")
	defines({ "_UNIX", "UNIX", "LINUX" })
end

-- config for debug build.
filter({ "configurations:Debug" })
defines({ "DEBUG" })
symbols("On")
warnings("Extra") -- Show extra warnings in  mode
links({})

-- config for release build.
filter({ "configurations:Release" })
defines({ "NDEBUG" })
optimize("Full")
flags({ "LinkTimeOptimization" }) -- Enable link-time optimization
links({})
