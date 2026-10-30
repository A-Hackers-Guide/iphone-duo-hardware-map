# `GpsDevice`

- Image: [`/System/Library/PrivateFrameworks/CoreGPSTest.framework/CoreGPSTest.dylib`](../userland/System__Library__PrivateFrameworks__CoreGPSTest.framework__CoreGPSTest.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
^v _fTestDevice;
{Options="uartPortName"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"gnssDeviceLibraryName"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"logLevel"I"secondaryLogLevel"I"logMask"Q"clearNvStore"B"printNmeaMessage"B"hostPassThroughMode"B"doPeriodic"B"doCw"B"doModulated"B"doRecordIQ"B"doPowerMode"B"doHostWakeGpio"B"doTimeMarkGpio"B"doCommPing"B"doCommLoopback"B"bandLteFilter"{optional<int>=""(?="__null_state_"c"__val_"i)"__engaged_"B}"l5NotchFilter"{optional<bool>=""(?="__null_state_"c"__val_"B)"__engaged_"B}"blanking"{optional<GnssHal::ExtensionsFire::BlankingSetting>=""(?="__null_state_"c"__val_"C)"__engaged_"B}"periodicDurationSec"i"cwDurationSec"i"cwBandwidthHz"i"integrationTimeMilliseconds"i"band"C"subband"(Subband="prn"i"fcn"i)"modulatedDurationSec"i"recordIQDurationSec"i"powerMode"i"hostWakeGpioTimeoutMs"i"timeMarkGpioTimeoutMs"i"commPingTimeoutMs"i"commLoopbackTimeoutSec"i"extraOptions"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"uartBaudRate"i} _fTestOptions;
```

## Properties

```
@property (T^v,V_fTestDevice) fTestDevice;
@property (T{Options={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}IIQBBBBBBBBBBBB{optional<int>=(?=ci)B}{optional<bool>=(?=cB)B}{optional<GnssHal::ExtensionsFire::BlankingSetting>=(?=cC)B}iiiiC(Subband=ii)iiiiiii{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}i},V_fTestOptions) fTestOptions;
```

## Instance methods

```
-[GpsDevice dealloc];
-[GpsDevice init:];
-[GpsDevice flushLogs];
-[GpsDevice setFTestDevice:];
-[GpsDevice fTestDevice];
-[GpsDevice fTestOptions];
-[GpsDevice getGpsConfiguration:error:];
-[GpsDevice setFTestOptions:];
-[GpsDevice testApSignalGpio:];
-[GpsDevice testCommPing:error:];
-[GpsDevice testCommPing:id:error:];
-[GpsDevice testExternalFreqAssistance:];
-[GpsDevice testGpsCw:error:];
-[GpsDevice testGpsModulated:gpsPrn:error:];
-[GpsDevice testPeriodic:error:];
-[GpsDevice testPowerMode:error:];
-[GpsDevice testTimeMarkGpio:];
```
