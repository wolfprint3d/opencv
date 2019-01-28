
# This file is auto-generated by mama build. Do not modify by hand!
if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(CLANG TRUE)
elseif(CMAKE_CXX_COMPILER_ID MATCHES "GNU")
    set(GCC TRUE)
endif()
set(MAMA_INCLUDE "")
set(MAMA_LIBS "")
if(ANDROID OR ANDROID_NDK)
    set(MAMA_BUILD "android")
    
elseif(WIN32)
    set(MAMA_BUILD "windows")
    
elseif(APPLE)
  if(IOS_PLATFORM)
    set(IOS TRUE)
    set(MAMA_BUILD "ios")
    
  else()
    set(MACOS TRUE)
    set(MAMA_BUILD "macos")
    
  endif()
elseif(RASPI)
    set(MAMA_BUILD "raspi")
    
elseif(UNIX)
    set(LINUX TRUE)
    set(MAMA_BUILD "linux")
    
else()
    message(FATAL_ERROR "mama build: Unsupported Platform!")
    set(MAMA_BUILD "???")
endif()

if(MSVC)
    add_definitions(-D_ITERATOR_DEBUG_LEVEL=0)
    foreach(MODE "_DEBUG" "_MINSIZEREL" "_RELEASE" "_RELWITHDEBINFO")
        string(REPLACE "/MDd" "/MD" TMP "${CMAKE_C_FLAGS${MODE}}")
        set(CMAKE_C_FLAGS${MODE} "${TMP}" CACHE STRING "" FORCE)
        string(REPLACE "/MDd" "/MD" TMP "${CMAKE_CXX_FLAGS${MODE}}")
        set(CMAKE_CXX_FLAGS${MODE} "${TMP}" CACHE STRING "" FORCE)
    endforeach(MODE)
endif()
