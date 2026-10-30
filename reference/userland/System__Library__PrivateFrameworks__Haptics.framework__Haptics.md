# `/System/Library/PrivateFrameworks/Haptics.framework/Haptics`

iOS 27.2 dyld shared cache image. Version `37.0.0.0.0`. **[DSC]**

## Linked libraries (10)

- `/System/Library/PrivateFrameworks/caulk.framework/caulk`
- `/System/Library/PrivateFrameworks/AppleSauce.framework/AppleSauce`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 1 classes, 0 protocols, 11 methods, 2 properties

### Class pages

Every class and protocol, with its methods: [`HAButtonHapticsLoader`](../objc/HAButtonHapticsLoader_Haptics.md)

### Classes

`HAButtonHapticsLoader`

### Properties

```
@property (Tq,R,N) maxNumberOfSlots;
@property (TB,R,N) serviceAvailable;
```

## Strings (91)

```
States
HapticGain
Default
/
displayname
[%u]
AudioPreSilence
AudioGain
Variant1.SingleClick.SemiSoft
Variant2.SecondClick.Normal
Variant3.SecondClick.SemiSoft
Variant3.SecondClick.Soft
v8@?0
.plist
%s
Variant3.SecondClick.Normal
HAButtonHapticsLoader.mm
Button Haptics Asset Interface
Could not construct
'%s' | <unknown type id: %d)>\n
'%s' | String{%d} | \"%s\"\n
'%s' | %sData{%d} | %d bytes\n
HAButtonHapticsLoaderServiceIsAvailableNotification
void MatchingNotificationHandler(void *, io_iterator_t)
result
'%s' | Number(SInt16){%d} | 0x%04x\n
Variant2.SingleClick.Normal
/Library/Audio/Tunings
FAIL
result = AudioFileReadBytes(afid, true, 0, &numBytes, buttonInfo.audioWaveformBuffer)
basic_string
com.apple.coreaudio.utility
*** done.\n
'%s' | Number(SInt32){%d} | %-6d 0x%08x %c%c%c%c\n
'%s' | Dictionary{%d} | %d key/value pairs\n
Variant2.SecondClick.Soft
Latch
result = AudioFileGetProperty(afid, kAudioFilePropertyAudioDataByteCount, &propSize, &numBytes64)
Error loading plist file 
AudioFilePath
HapticFilePath
Variant1.SecondClick.SemiSoft
'%s' | Array{%d} | %d ordered objects\n
buttonhapticsconfig
result = AudioFileReadBytes(afid, true, 0, &numBytes, buttonInfo.hapticWaveformBuffer)
name
@@ Strips Oct  3 2026 17:33:33
\n
aupreset
AUPreset
TPLM
result = AudioFileGetProperty(afid, kAudioFilePropertyDataFormat, &propSize, &fmt)
PostSilence
DownGain
Variant1.SecondClick.Normal
Variant3.SingleClick.Normal
Variant3.SingleClick.SemiSoft
IOServiceMatched
vector
Variant1.SingleClick.Soft
UpGain
Variant1.SingleClick.Normal
Variant2.SecondClick.SemiSoft
result = dictForType(type, typeDictionary)
Variant2.SingleClick.SemiSoft
Variant3.SingleClick.Soft
'%s' | Number(SInt8){%d} | 0x%02x\n
HapticPreSilence
Variant1.SecondClick.Soft
Variant2.SingleClick.Soft
IOPropertyMatch
.propstrip
TuningPListMgr.cpp
'%s' | Number(float){%d} | %f\n
ButtonHaptics
.austrip
.aupreset
getAUPListByName failed
get typeDictionary failed
%s Unable to open user client err %d
Haptics IONotificationPortGetRunLoopSource returned NULL
Haptics CFRunLoopGetCurrent returned NULL
%25s:%-5d  ca_require_noerr: [%s, %d] (goto %s;)
Haptics IOConnectCallStructMethod UpdateSSHBAsset err %d
get statesDictionary failed
bad typeKey
%s failed to send GetNumberOfSupportedAssets err %d
Haptics IOServiceAddMatchingNotification err %d
Haptics loadButtonHapticOfType FAILED %d
%25s:%-5d return dictionary is null
loadTuning failed %d
```
