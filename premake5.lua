 
-- premake5.lua
workspace "game"
	configurations { "Debug", "Release" }
    architecture "x86_64"
    cppdialect "C++latest"

project "Application"
	kind "ConsoleApp"
	language "C++"
    cppdialect "C++latest"
	targetdir "bin/%{cfg.buildcfg}"
	 
	files { "src/*.h", "src/*.cpp" }

    --WINDOWS

    -- config for windows debug build.
	filter {"configurations:Debug","system:windows"}
	     defines { "DEBUG", "_WIN32"}
	     symbols "On"
	     warnings "Extra"  -- Show extra warnings in  mode
		--link locally installed libraries
		includedirs{"dependencies/".. os.target() .. "/include"}
		libdirs{"dependencies/".. os.target() .. "/lib"}
		links {}



    -- config for windows release build.
	filter { "configurations:Release", "system:windows" }
		defines { "NDEBUG", "_WIN32" }
		optimize "On"
		--link locally installed libraries
		includedirs{"dependencies/".. os.target() .. "/include"}
		libdirs{"dependencies/".. os.target() .. "/lib"}
		links {}

        --LINUX

    -- config for linux debug build.
	filter {"configurations:Debug","system:linux"}
		defines { "DEBUG","_UNIX"}
		symbols "On"
		warnings "Extra"  -- Show extra warnings in  mode
		--link locally installed libraries
		includedirs{"dependencies/".. os.target() .. "/include"}
		libdirs{"dependencies/".. os.target() .. "/lib"}
		links {}


    -- config for linux release build.
	filter { "configurations:Release", "system:linux" }
		defines { "NDEBUG", "_UNIX" }
		optimize "On"
		flags { "LinkTimeOptimization" } -- Enable link-time optimization
		--link locally installed libraries
		includedirs{"dependencies/".. os.target() .. "/include"}
		libdirs{"dependencies/".. os.target() .. "/lib"}
		links {}

