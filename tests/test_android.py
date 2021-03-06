#!/usr/bin/env python
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
"""
Functional tests for the SCons Android tool
"""

import sconstester
import os
import sys
import base64
import StringIO

# print base64.encodestring(open("filename").read())
# using stock android icon

_ICON_DATA = """\
iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAJ1UlEQVRoBe1ZW5AUVxn+untmd5iZ
ZZdd9sIu14VAAJclAbJi0DImIZbltRJCES2txLLUirHUlOVLHqgyLwpqqUmpD0nKkhijFJYxliUv
kAARIiCbDZcQlh0uy7IX9jb3S3f7/T3Ty8xOT89AyPLiX/XP6T7n9H/++/nPGeD/cHs1oFS4fKXz
KiRX8TSz3MxSjEm/SvQQq3KosbX7+fihgUHKwrhOTOUww9bu5+N1EAadQJj3EgObHqnrWLk++Lyh
ZKpgqqUEdqJx832KYaqmJ3X6aOTJg7vHe0goSkwTRagCKMVQNWcFfvjrjz5T16h+O2OkfQVfzdCL
R/UmxoeN3+x46vCzXFKEEIsUuFUpC4jbBFqWKZtbFgZ8plnwDYdmBhRF8V29GNnM1X5BFAuIAAXg
JIBYRSwQnAyHTX8sBdMQ96PoFCSNBKqVWYVqsEYlQBToZgaqIh7oZFyFtOgFHFIUCSkDGTMJr+Jz
pqeqmAwnRXtBYjyHEg9TICs5gVD3mrqhWV5ncEXKUK3W4s76z1EQeRdmTAut8OJ7IhXBRxofhV+b
B2Nq7Pq8dCaJBXX3os63GLqeseh95o7nkBEFWWtk6U49U1aLh2w82kmkgF8nC8gEEawqk1JUYURQ
JOha/BTm+u/ARHQAw9FTuLvt62gKrsJbF36JSGIAn13xHPzeOegbOYA7G76I+bX34Hj/S+ho2YJg
1Ty8dupb0DM6UpkU2oJdWNX8JTT6V8FIk75a7KY0AIQH4SXHE5tCKGUBqsJSuuU24jqGbqA1uJ7M
Po/2hvuR1lNY07INl8aOoL3+fjTVdGIk+j6iqRFqNIlF1PRYLATDNODz1KN/8hhaZ98Df1Uzgp4W
bFz4XfRPHIOmeOg+xtQ6slY+Zp3XYtriqZD9rKan98m7NTmZCiOWmEScaBoqUvok2us+heUNnyYT
rRgKn0HPlT1IG2mOK+i7dhDD4V4kkjEk0jH8u++3CMeG2XcOF0ePUMlVSKYmkM4kLDfsHX6Dz8mp
NWSdfJS1hYccCE9FQpRyIeubNS1bsXRRC7WfRtDXisn4AC5NvI32ufdhU/v3UVPdig0LHkfL7LWY
pdWiY94j9D2PtUpDYBm6Fn6DwiWxtm0b1rRuwTv9r2COfykiqSEGMbDt7lfgVX3YuOjJXFDbvGZb
ldtOb+wqX3YUDuS9FUnEMelrJc47duy/uzo7O1boetH+kUfiw3vUNA3d3T3vrVt311e4ygBxmFiQ
SkvFQI6rPA/M9cx8486DqwtZwcsUJ+3tAKOCtV0FEKbtjHA7BKhEca4CiO+LFgRvF5SLP1cBbKYr
0YQ9d6bbsgLcSguwOKN8LC24uVUC2fnuM12z0K3WvCgjkZlw52jaaDkeXAUQWrYFbkWb1uM4FPqJ
VVuVoyfaT6e5gQaDtTU1NXK4coSyLiQaKKcFR8rTOoUhyyVYRkvZbdMk9YKZ9rxIJIIrV65gYGBA
eBRFO2261pm3gED+i2jAzkT5/Tf6rLFc8PCEmtQjrH3iGEtcYCk9GwFvo8V+xpBSPwsqS1BhfHBw
ULQvnRmCtNkAkqc8KGuBvLk3/KiI4qj5ixOHcGF8H/rDbyOWHsbl04d56KlmSb0eS+bchyUsEK3g
ZlUqrjU6OgoRRICWUgWtCQ5WcBVAtC+mFqLuYLIoq4ZuZIQFWRYedRZ6Bv+IE4O/ZxWbrSgtgahI
3ZRyJoXQ+JsU7E0cUH+KDfO+iZVND/NLHclkEh6Ph0LyDFPoYUVsZMUs6r6xDg+1eXHiCKLpES7q
gYdHRNH6W5d2IpmZJDFZRrV4kRT68YXP4JOLtpM5xgL703oMBy/twHg8RPFUeL1epOi+Q9HTmEhe
dhXB1QKifbFCud1Q5zm52d+J90Zf58HlP6jWanD22t+gqX7xgamAzapFoebfsM7NHLLGFWg8K6h4
tWcrHl71MpavWIaX9j+BsZEI1ESDY/BmaWUvruxnx1aEEHQHGVfQ0bgVzcFO7Dn1GF1IbmKcvwuN
7bPGNLqZgG6mKawPn5j/NNfSMZnohzY3hGoekkLvXo4kEgmJYiFWRNDVAnauLi+AUDaR4UH9zNBf
oZk+ukWcIok78T5s2roqstdMGc4RIR5cspMzDBwMPYuYPo6tq3ejpXoD1IZuNLYxsHKnWycBXGOg
Mu2TLEFyezQ5iPOj+6wgXd24DU2B1QzspHjRNJRQ1zG/5l5sXvpz9I3vx95zTyOuRyUC0D34MtYx
qOW2gnFsa75I+7KuqwVkgkD5LCQCqAhNHECYtxNyTExloowd3kXlLStaloBdMffzWN24BSeuvoh/
nf0Bp0go8yoqN/fk1T/ziFqPet8y9GdOWCxYjDj8uFpA5ttWKNcaVHM4yfMrQ05RvTg78ndci53l
i7hQVuMas9Oa5q9i6ZyHcOjiTgbzAYt5ax3rSURhCtZ8ODm8m7cej5FcngamRLwuiasFhGk7Dq5/
4vwkqcIQd5VtQDGZV7IaNSVANT/uan4c1Z46vDO0CyeH/kKNS+7hHMcthjcgRhjx5DjjYwd+hUed
F2VvWQuU/HLagGgu4OUNBoUWncmvZJeaqjY8tPRn3JA92N+3fSrXmzndZudmVZv/LKx1D+4iDauM
sFcrSqmuFpAaRCwgligPJhbUfgyBqkZebg2jyd+BTYt+hD4G9T/OfMcSycM7VZGuInIUMJ4aw77Q
j12XdhVAvrR935VKbjCgNWFx7QO8XqxH2+wuLr4dY/HzqFIDnFGkvApISgS4X+m4CnAjMaCpvL5k
adDV9j3sOf1lHBt4gT6u8ebZX6EFi+VRxB2te9niMbvHVQB7UrlWrsqvhrtxefIw3Wijlf/HE+ez
pUS5jz/guKsAtu/brdNaKoPt+JXfoWfoT1YFempkN76w/AXejY6xLjrK4L35PCGxUsYA7lnIDmA7
DpxaWWAk/j4ZlVMfmTU1blB/wNrmJ5gh6QK5oL2pVlKsY5q9rspS6uGyWXBiOr/PYPG1ikVcllPZ
AhSWE3txbmwv7/5XcjdOcoy0PgjmWMlRyb7lfl0FkMtV+4xauoWVPtvrH2QMk0smG482C+dG/4nO
5q9B1WgZSUA3gVbesn4sbqeUmi9BqRiQ3JU4fvz4WG9v7yT3AxGUSYHqdQQ5pC/Gu/2v5Y3qiDS8
Th/uQi8tIsVepUBOpTiSP3WNRNQc43cJomM+daIqffU5XM92MbGOKDVwyesNjt1KkH8khelxYoh4
lDhKlOOdjE2BkwAyKNcBsvs0EWcTa4gsXJjYZwZE2wweyGFamB4iyv/EggWuVMqFbA2I1HLnIUSE
+VIxw6FbCpJ7RAj7r1WxRoHm7dVKWUAYFYZFQLuVuTMpgGhaKjkRxG6Lkur/AEiaJNAV7ZR0AAAA
AElFTkSuQmCC
"""
_TOOL_SETUP = """
var = Variables('../variables.cache', ARGUMENTS)
var.AddVariables(
    ('ANDROID_KEY_STORE', 'Android keystore'),
    ('ANDROID_KEY_NAME', 'Android keyname'),
    ('ANDROID_NDK', 'Android NDK path'),
    ('ANDROID_SDK', 'Android SDK path'))
env = Environment(tools=['android'], variables=var)
var.Save('variables.cache', env)
"""

def getNDK():
    """
    Get the NDK variable, either the default or from the environment
    """
    if 'ANDROID_NDK' in os.environ:
        return os.environ['ANDROID_NDK']
    else:
        return os.path.expanduser('~/tools/android-ndk-r7b')

def getKeyStore():
    """
    Get the keystore variable, either the default debug keystore or from the
    environment
    """
    if 'ANDROID_KEY_STORE' in os.environ:
        return os.environ['ANDROID_KEY_STORE']
    else:
        return os.path.expanduser('~/.android/debug.keystore')

def getSDK():
    """
    Get the SDK variable, either the default or from the environment
    """
    if 'ANDROID_SDK' in os.environ:
        return os.environ['ANDROID_SDK']
    else:
        return os.path.expanduser('~/tools/android-sdk-linux_86')

def create_variant_build(tester, duplicate):
    """
    Add variant build boilerplate to a test
    """
    cwd = os.path.normpath(os.getcwd())
    rootdir = os.path.normpath(os.path.join(cwd, '..'))
    tester.write_file('SConstruct','''
from SCons import Tool
Tool.DefaultToolpath.append('%s')
SConscript('main.scons', variant_dir='build', duplicate=%d)\n''' % (rootdir, duplicate))

def create_resources(tester):
    tester.subdir('res/drawable')
    tester.subdir('res/layout')
    tester.subdir('res/values')
    tester.write_file('res/drawable/icon.png', base64.decodestring(_ICON_DATA))
    tester.write_file('res/values/strings.xml',
                      '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">My Test App</string>
</resources>''')

def create_activity(tester):
    srcdir = 'src/com/example/android'
    tester.subdir(srcdir)
    tester.write_file(srcdir + '/MyActivity.java',
                      '''
                      package com.example.android;
                      public class MyActivity {}
                      ''')
    return srcdir

def create_nocode_manifest(tester):
    tester.write_file('AndroidManifest.xml',
                      '''<?xml version="1.0" encoding="utf-8"?>
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android"
    android:installLocation="auto"
    android:versionCode="1"
    android:versionName="1.0" >
    <application
        android:hasCode="false"
        android:icon="@drawable/icon"
        android:label="@string/app_name">
        <activity
            android:name="android.app.NativeActivity"
            android:label="@string/app_name">
            <meta-data android:name="android.app.lib_name"
                    android:value="native-activity" />
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>
    <uses-sdk android:targetSdkVersion="13" android:minSdkVersion="9" />
</manifest>\n''')

def create_standard_manifest(tester):
    tester.write_file('AndroidManifest.xml',
                      '''<?xml version="1.0" encoding="utf-8"?>
<manifest
    xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.android"
    android:installLocation="auto"
    android:versionCode="1"
    android:versionName="1.0" >
    <application
        android:icon="@drawable/icon"
        android:label="@string/app_name">
        <activity
            android:name=".MyActivity"
            android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>
    <uses-sdk android:targetSdkVersion="10" android:minSdkVersion="4" />
</manifest>\n''')

def create_android_project(tester, duplicate=0):
    """
    Add an Android project to a test
    """
    create_variant_build(tester, duplicate)
    create_resources(tester)
    srcdir = create_activity(tester)
    create_standard_manifest(tester)

    return srcdir

def create_jni_stub(tester):
    tester.subdir('jni')
    tester.write_file('jni/test.c',
                      '''#include <android/log.h>
                      int not_really_jni(void) { return 1; }''')

def create_new_android_ndk_project(tester, duplicate=0):
    """
    Create a new-style NDK library Android project
    """
    create_android_project(tester, duplicate)
    create_jni_stub(tester)

def create_android_ndk_project(tester, duplicate=0):
    """
    Create a ndk-build NDK library Android project
    """
    create_new_android_ndk_project(tester, duplicate)
    tester.write_file('jni/Android.mk',
                      '''
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_SRC_FILES := test.c
LOCAL_MODULE := test
include $(BUILD_SHARED_LIBRARY)''')

class AndroidSconsTest(sconstester.SConsTestCase):
    """
    Test cases for the android.py tool
    """

    def testRuns(self):
        """
        Test the android tool doesn't cause a stacktrace
        """
        cwd = os.path.normpath(os.getcwd())
        rootdir = os.path.normpath(os.path.join(cwd, '..'))
        self.write_file('SConstruct','''
from SCons import Tool
var = Variables(None, ARGUMENTS)
var.AddVariables(('ANDROID_SDK', 'Android SDK path'))
Tool.DefaultToolpath.append('%s')
env = Environment(tools=['android'], variables=var)\n''' % (rootdir))
        result = self.run_scons(['ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)

    def testErrorWhenNoAndroidVariables(self):
        """
        Test that not setting android variables causes an error
        """
        cwd = os.path.normpath(os.getcwd())
        rootdir = os.path.normpath(os.path.join(cwd, '..'))
        self.write_file('SConstruct','''
from SCons import Tool
Tool.DefaultToolpath.append('%s')
env = Environment(tools=['android'])\n''' % (rootdir))
        # hide error message as failure is expected
        old_stdout = sys.stdout
        sys.stdout = StringIO.StringIO()
        try:
            result = self.run_scons(['ANDROID_SDK='+getSDK()])
            self.assertEquals(1, result.return_code)
            self.assertEquals(result.out[1], ('Please set ANDROID_SDK. '
                                       'export ANDROID_SDK=path\n'))
        finally:
            sys.stdout = old_stdout

    def checkBasicBuild(self, duplicate):
        create_android_project(self, duplicate)

        self.write_file('main.scons','''
var = Variables(None, ARGUMENTS)
var.AddVariables(('ANDROID_SDK', 'Android SDK path'))
env = Environment(tools=['android'], variables=var)
env.AndroidApp('Test')
''')
        result = self.run_scons(['ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test-debug.apk'))

    def testBasicBuildDir(self):
        """
        Test that a simple compile works, produces apk file
        """
        self.checkBasicBuild(0)
        self.checkBasicBuild(1)

    def checkBasicNdkBuild(self, duplicate):
        """
        Test that a compile with NDK works, produces apk file
        """
        create_android_ndk_project(self, duplicate)

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuildLegacy('libs/armeabi/libtest.so', ['jni/test.c'])
apk = env.AndroidApp('Test', native_folder='#libs')
env.Help(var.GenerateHelpText(env))
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.exists('libs/armeabi/libtest.so', variant=''))
        self.assertTrue(self.apk_contains('Test-debug.apk', 'lib/armeabi/libtest.so'))
        # check that a rebuild is a no-op
        result = self.run_scons()
        self.assertEquals("scons: `.' is up to date.\n", result.out[4])

    def testBasicNdkBuild(self):
        """
        Test that a compile with NDK works, produces apk file
        """
        self.checkBasicNdkBuild(0)
        self.checkBasicNdkBuild(1)

    def testDefaultProperties(self):
        """
        Test that default.properties file with empty lines works
        """
        create_android_ndk_project(self)
        self.write_file('default.properties','''
#blank line test

target=android-13
''')

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuildLegacy('libs/armeabi/libtest.so', ['jni/test.c'])
apk = env.AndroidApp('Test', native_folder='#libs')
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)


    def testGeneratedRes(self):
        """
        Test that generated resources work
        """
        srcdir = create_android_project(self)
        self.write_file(srcdir + '/MyActivity.java',
                          '''
                          package com.example.android;
                          public class MyActivity {
                              public void onCreate() {
                                // make sure this gets used
                                System.out.println(R.raw.fake);
                              }
                          }
                          ''')
        self.subdir('sounds')
        self.write_file('sounds/fake.wav', '''BAM''')

        self.write_file('main.scons', _TOOL_SETUP + '''
env.Command('res/raw/fake.ogg', 'sounds/fake.wav',
    [Mkdir('res/raw'), Copy('$TARGET', '$SOURCE')])
env.AndroidApp('Test', resources=['res','#res'])
''')
        result = self.run_scons(['ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.apk_contains('Test-debug.apk', 'res/drawable/icon.png'))
        self.assertTrue(self.apk_contains('Test-debug.apk', 'res/raw/fake.ogg'))
        # check rebuild is a no-op
        result = self.run_scons()
        self.assertEquals("scons: `.' is up to date.\n", result.out[4])
        # check that adding a resource is a rebuild
        self.write_file('sounds/fake.wav', '''BAR''')
        result = self.run_scons()
        self.assertEquals('Copy("build/res/raw/fake.ogg", "sounds/fake.wav")\n', result.out[5])

    def testNewNdkBuild(self):
        """
        Test that a compile with the new NDK build works,
        and is comparable with the legacy Android.mk system
        """
        create_android_ndk_project(self)

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuildLegacy('libs/armeabi/libtest.so', ['jni/test.c'])
env.NdkBuild('new/libtest.so', ['jni/test.c'])
apk = env.AndroidApp('Test', native_folder='#libs')
env.Help(var.GenerateHelpText(env))
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.exists('libs/armeabi/libtest.so', variant=''))
        self.assertTrue(self.exists('new/libtest.so'))
        oldsize = len(self.get_file('libs/armeabi/libtest.so', variant='').read())
        newsize = len(self.get_file('new/libtest.so').read())
        self.assertTrue(oldsize >= newsize, '%d >= %d failed' % (oldsize, newsize))

    def testCplusplusNdkBuild(self):
        """
        Test that a compile with the new NDK build works,
        and is comparable with the legacy Android.mk system
        """
        create_new_android_ndk_project(self)
        self.write_file('jni/test.cpp',
                        '''#include <android/log.h>
                        class Foo {public: int i;};
                        int do_foo(const Foo &f) {return f.i;}''')

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuild('libs/armeabi/libtest.so', ['jni/test.cpp'])
apk = env.AndroidApp('Test', native_folder='libs')
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.exists('libs/armeabi/libtest.so'))
        # check the CXX command line has -fno-rtti, -mthumb at least
        compile_line = ''
        for line in result.out:
            comps = line.split()
            if len(comps) and comps[0].endswith('arm-linux-androideabi-g++'):
                compile_line = line.strip()
                break
        self.assertNotEquals('', compile_line)
        msg = 'compile line "%s"' % compile_line
        self.assertTrue('-fno-rtti' in compile_line, msg)
        self.assertTrue('-fno-exceptions' in compile_line, msg)
        self.assertTrue('-mthumb' in compile_line, msg)

    def checkLibraryAssembler(self, name, instruction):
        """
        Check the disassembled library contents for the instruction snippet.
        Uses objdump on the command line to do this.
        """
        libtest = self.get_file(name)
        libtest.close()
        objdump = getNDK() + ("/toolchains/arm-linux-androideabi-4.4.3/prebuilt"
                              "/linux-x86/bin/arm-linux-androideabi-objdump")
        # check the decompiled code contains instruction
        prog = sconstester.Popen([objdump, '-d', libtest.name],
                                 shell=False,
                                 stdout=sconstester.PIPE,
                                 stderr=sconstester.PIPE)
        result = prog.stdout.read()
        return_code = prog.wait()
        self.assertEquals(0, return_code)
        self.assertTrue(result.find(instruction) != -1,
                        '"%s" not found in disassembly' % instruction)

    def checkLibraryArch(self, name, arch):
        """
        Check if a library is the given arch using the file utility
        """
        libtest = self.get_file(name)
        libtest.close()
        # check is an intel library
        prog = sconstester.Popen(['file', libtest.name],
                                 shell=False,
                                 stdout=sconstester.PIPE,
                                 stderr=sconstester.PIPE)
        result = prog.stdout.read()
        return_code = prog.wait()
        self.assertEquals(0, return_code)
        self.assertTrue(result.find(arch) != -1, result.strip())

    def checkMultiAbiBuild(self, app_abi):
        """
        Test that a compile for x86 works. Needs NDK r6+
        """
        create_new_android_ndk_project(self)

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuild('libtest.so', ['jni/test.c'], app_abi=%s)
apk = env.AndroidApp('Test', native_folder='libs')
env.Help(var.GenerateHelpText(env))
''' % app_abi)
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.checkLibraryArch('libs/armeabi/libtest.so', 'ARM')
        self.checkLibraryArch('libs/x86/libtest.so', 'Intel')

        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.exists('libs/armeabi/libtest.so'))
        self.assertTrue(self.exists('libs/x86/libtest.so'))
        self.assertTrue(self.apk_contains('Test-debug.apk', 'lib/x86/libtest.so'))

    def testX86NdkBuild(self):
        self.checkMultiAbiBuild("'armeabi x86'")
        self.checkMultiAbiBuild('["armeabi", "x86"]')

    def testV7aNdkBuild(self):
        """
        Test that a compile for v7a works.
        """
        create_new_android_ndk_project(self)
        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuild('libs/armeabi-v7a/libtest.so', ['jni/test.c'], app_abi='armeabi-v7a')
apk = env.AndroidApp('Test', native_folder='libs')
''')
        self.write_file('jni/test.c', '''#include <android/log.h>
                int foo[] = {
                        1,
                        2,
                        3,
                        9,
                        15
                };

                int not_really_jni(int a) {
                        int x = a / foo[a];
                        return x;
                } ''')

        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        libname = 'libs/armeabi-v7a/libtest.so'
        self.checkLibraryArch(libname, 'ARM')
        # arm v7a (thumb2) includes shifted offset instructions
        # ldr.w r1, [r3, r0, lsl #2]
        # whereas thumb 1 has to do this in 2 steps
        # lsl r2, r0, #2
        # ldr r1, [r3, r2]
        self.checkLibraryAssembler(libname, ', lsl #2]')

        self.assertTrue(self.exists('Test-debug.apk'))
        self.assertTrue(self.exists('libs/armeabi-v7a/libtest.so'))
        self.assertTrue(self.apk_contains('Test-debug.apk', 'lib/armeabi-v7a/libtest.so'))

    def testMultipleAPKs(self):
        """
        Test that multiple APKs can be built
        """
        create_new_android_ndk_project(self)

        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuild(['arm/armeabi/libtest.so', 'intel/x86/libtest.so'],
                        ['jni/test.c'], app_abi='armeabi x86')
env.AndroidApp('TestArm', native_folder='arm')
env.AndroidApp('TestIntel', native_folder='intel')
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)

        self.assertTrue(self.exists('TestArm-debug.apk'))
        self.assertTrue(self.exists('arm/armeabi/libtest.so'))
        self.assertTrue(self.exists('intel/x86/libtest.so'))
        self.assertTrue(self.apk_contains('TestArm-debug.apk', 'lib/armeabi/libtest.so'))
        self.assertFalse(self.apk_contains('TestArm-debug.apk', 'lib/x86/libtest.so'))

        self.assertFalse(self.apk_contains('TestIntel-debug.apk', 'lib/armeabi/libtest.so'))
        self.assertTrue(self.apk_contains('TestIntel-debug.apk', 'lib/x86/libtest.so'))

        # ensure no errors on null build (R.java bug)
        result = self.run_scons()
        self.assertEquals([], result.err)

    def testCFLAGS(self):
        """
        Test that CFLAGS and CXXFLAGS are flat arrays
        """
        create_new_android_ndk_project(self)
        self.write_file('main.scons', _TOOL_SETUP + '''
lib = env.NdkBuild('libs/armeabi/libtest.so', ['jni/test.c'])
print len(env['CFLAGS'])
print len(env['CXXFLAGS'])
''')
        result = self.run_scons(['-Q', 'ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        cflags_len = result.out[0].strip()
        self.assertEquals('19', cflags_len,
              "Expected CFLAGS to contain 19 entries (%s)" % cflags_len)
        cxxflags_len = result.out[1].strip()
        self.assertEquals('21', cxxflags_len,
              "Expected CXXFLAGS to contain 21 entries (%s)" % cxxflags_len)

    def testCPPPATH(self):
        create_new_android_ndk_project(self)
        self.subdir('jni/subdir')
        self.write_file('jni/subdir/foo.h', '''\
#define FOO 1
''')
        self.write_file('jni/test2.c', '''\
#include "foo.h"
''')
        self.write_file('main.scons', _TOOL_SETUP + '''
env.MergeFlags('-Ijni/subdir')
lib = env.NdkBuild('libs/armeabi/libtest.so', ['jni/test.c', 'jni/test2.c'])
''')
        result = self.run_scons(['-Q', 'ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)

    def testExternalJar(self):
        create_new_android_ndk_project(self)
        self.subdir('external_jar/src/com/example')
        self.write_file('external_jar/src/com/example/Hello.java', '''\
package com.example;

public class Hello {
    public Hello() {}
    public String getMessage() { return "Hello"; }
}
''')
        self.write_file('external_jar/SConstruct', '''\
env = Environment()
classes = env.Java(target='classes', source='src')
env.Jar(target='test_lib.jar', source=classes)
''')
        result = self.run_scons(['-C', 'external_jar'])
        self.assertEquals(0, result.return_code)
        # check the external jarfile is created..
        self.assertTrue(self.exists('external_jar/test_lib.jar', '.'))

        # now make sure we link with it in an Android project...
        self.write_file('main.scons', _TOOL_SETUP + '''
env['JAVACLASSPATH'] = 'external_jar/test_lib.jar'
env.AndroidApp('TestExternalJar')
''')
        self.write_file('src/com/example/android/MyActivity.java',
                          '''
                          package com.example.android;
                          import com.example.Hello;
                          public class MyActivity {}
                          ''')
        result = self.run_scons(['ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)

    def testNdkNativeActivity(self):
        """
        Test the android:hasCode=false case for native activities
        """
        create_variant_build(self, duplicate=1)
        create_resources(self)
        create_nocode_manifest(self)
        self.subdir('jni')
        self.write_file('jni/test.c','''\
#include <android/log.h>
#include <android_native_app_glue.h>

void android_main(struct android_app *state)
{
	app_dummy();
}
''')
        self.write_file('main.scons', _TOOL_SETUP + '''
env.Repository('$ANDROID_NDK/sources')
env['CPPPATH'] = ['android/native_app_glue']
env.MergeFlags('-llog -landroid')
lib = env.NdkBuild('libtest.so', ['jni/test.c', Glob('android/native_app_glue/*.c')])
apk = env.AndroidApp('Test')
''')
        result = self.run_scons(['ANDROID_NDK='+getNDK(), 'ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        # check the apk contains *something*
        self.assertTrue(self.apk_contains('Test-debug.apk', 'lib/armeabi/libtest.so'))

    def testProguard(self):
        create_new_android_ndk_project(self)

        self.write_file('src/com/example/android/MyActivity.java',
                          '''\
package com.example.android;
import android.app.Activity;

public class MyActivity extends Activity {
}
''')
        self.write_file('main.scons', _TOOL_SETUP + '''
env['PROGUARD_CONFIG'] = '$ANDROID_SDK/tools/proguard/proguard-android.txt:proguard-project.txt'
env['JARSIGNER_FLAGS'] = ' -storepass android -keypass android'
apk = env.AndroidApp('Test')
''')
        result = self.run_scons(['ANDROID_SDK='+getSDK(), 'ANDROID_KEY_STORE='+getKeyStore(),
                                'ANDROID_KEY_NAME=androiddebugkey'])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('proguard/Testobfuscated.jar'))
        # make sure the size went down...
        self.assertTrue(self.filesize('proguard/Testobfuscated.jar') < self.filesize('proguard/Testoriginal.jar'))

        # make sure dex uses the obfuscated jar file..
        dex_line = [line.strip() for line in result.out if line.find('dx --dex --output') != -1]
        self.assertEquals(1, len(dex_line))
        self.assertEquals(True, dex_line[0].endswith('obfuscated.jar'), dex_line[0])

    def testAnnotations(self):
        create_android_project(self)

        self.write_file('src/com/example/android/MyActivity.java',
                          '''
                          package com.example.android;
                          import android.annotation.TargetApi;
                          public class MyActivity {
                              @TargetApi(8)
                              public void onCreate() {
                              }
                          }
                          ''')
        self.write_file('main.scons', _TOOL_SETUP + '''
env.AndroidApp('Test')
''')
        result = self.run_scons(['ANDROID_SDK='+getSDK()])
        self.assertEquals(0, result.return_code)
        self.assertTrue(self.exists('Test_bin/classes/com/example/android/MyActivity.class'))

if __name__ == '__main__':
    sconstester.unittest.main()
