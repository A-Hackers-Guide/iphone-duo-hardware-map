# `ABDNetwork`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
r^{?=QQ*} _shapeConfig;
{ABDNetworkRunner="_vptr$NetworkRunner"^^?"_valid"B"_stream"^{e5rt_execution_stream}"_networkVersion"@"NSString""_ops"@"NSArray""_operation"^{e5rt_execution_stream_operation}} _runner;
^{NetworkInputDescriptor=B*I} _inputDescriptor;
^{NetworkInputDescriptor=B*I} _coordinatesDescriptor;
^{NetworkInputDescriptor=B*I} _scalarsDescriptor;
^{NetworkOutputDescriptor=B*I} _outputDescriptor;
^{__CVBuffer=} _coordinateMap;
^{__CVBuffer=} _scalarsBuffer;
{ABDNetworkScalarMatrix="_valid"B"_values"[24[4f]]} _scalarsMatrix;
@"NSUserDefaults" _userDefaults;
@"NSString" _versionName;
@"NSString" _networkName;
@"ABDNetworkNoiseAddback" _noiseAddback;
```

## Properties

```
@property (T@"NSString",&,V_versionName) versionName;
@property (T@"NSString",&,V_networkName) networkName;
@property (T@"ABDNetworkNoiseAddback",&,V_noiseAddback) noiseAddback;
@property (TQ,R) width;
@property (TQ,R) height;
```

## Instance methods

```
-[ABDNetwork networkName];
-[ABDNetwork dealloc];
-[ABDNetwork setVersionName:];
-[ABDNetwork versionName];
-[ABDNetwork width];
-[ABDNetwork setNetworkName:];
-[ABDNetwork height];
-[ABDNetwork executeWithInput:into:with:];
-[ABDNetwork getNoiseAddbackFactor:];
-[ABDNetwork initWithBundleName:width:height:atPath:];
-[ABDNetwork noiseAddback];
-[ABDNetwork setNoiseAddback:];
```
