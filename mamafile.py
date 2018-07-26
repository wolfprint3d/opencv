import mama
class opencv(mama.BuildTarget):
    def dependencies(self):
        # custom mamafile can be passed explicitly:
        #self.add_git('zlib', 'https://github.com/madler/zlib.git', mamafile='zlib.py')
        pass

    def configure(self):
        opt = [
            "ENABLE_OMIT_FRAME_POINTER=ON", "ENABLE_PRECOMPILED_HEADERS=ON", "ENABLE_CCACHE=ON",
            "BUILD_DOCS=OFF",  "BUILD_EXAMPLES=OFF", "BUILD_TESTS=OFF", "BUILD_PERF_TESTS=OFF",
            "WITH_OPENGL=ON",  "WITH_IPP=OFF",    "WITH_OPENCL=OFF", "WITH_1394=OFF",    "WITH_CUDA=OFF",
            "WITH_OPENGL=ON",  "WITH_JASPER=OFF", "WITH_WEBP=OFF",   "WITH_OPENEXR=OFF", "WITH_TIFF=OFF", "WITH_FFMPEG=OFF",
            "BUILD_OPENEXR=OFF", "BUILD_TIFF=OFF", "BUILD_JPEG=ON",
            "BUILD_PNG=ON",      "BUILD_ZLIB=ON",  "BUILD_JASPER=OFF",
            "BUILD_opencv_apps=OFF",      "BUILD_opencv_calib3d=ON",   "BUILD_opencv_core=ON",
            "BUILD_opencv_features2d=ON", "BUILD_opencv_flann=ON",     "BUILD_opencv_highgui=ON",
            "BUILD_opencv_imgcodecs=ON",  "BUILD_opencv_imgproc=ON",   "BUILD_opencv_ml=ON",
            "BUILD_opencv_objdetect=ON",  "BUILD_opencv_photo=ON",    "BUILD_opencv_shape=OFF",
            "BUILD_opencv_stitching=OFF", "BUILD_opencv_superres=OFF", "BUILD_opencv_ts=OFF",
            "BUILD_opencv_video=ON",      "BUILD_opencv_videoio=ON",   "BUILD_opencv_videostab=OFF",
            "BUILD_opencv_nonfree=OFF", "BUILD_SHARED_LIBS=OFF", "BUILD_opencv_java=OFF", 
            "BUILD_opencv_python2=OFF", "BUILD_opencv_python3=OFF", "BUILD_opencv_xphoto=ON"
        ]
        if   self.config.android: opt += ['BUILD_ANDROID_EXAMPLES=OFF', 'BUILD_opencv_androidcamera=ON']
        elif self.config.ios:     opt += ['IOS_ARCH=arm64']
        elif self.config.windows: opt += ['BUILD_WITH_STATIC_CRT=OFF']
        elif self.config.macos:   opt += ['WITH_GSTREAMER=OFF', 'WITH_GPHOTO2=OFF']
        elif self.config.linux:   opt += []
        self.add_cmake_options(opt)
        self.cmake_build_type = 'Release'
        self.cmake_ios_toolchain = '../platforms/ios/cmake/Toolchains/Toolchain-iPhoneOS_Xcode.cmake'
        if self.config.ios:
            self.enable_ninja_build = False # opencv for ios blows up with Ninja

    def package(self):
       self.export_libs('lib', order=['xphoto','calib3d','features2d','flann', 'objdetect', 'photo', 'imgcodecs', 'imgproc', 'highgui', 'video', 'videoio', 'core'])
       self.export_libs('3rdparty/lib')
       self.export_include('include', build_dir=True)
