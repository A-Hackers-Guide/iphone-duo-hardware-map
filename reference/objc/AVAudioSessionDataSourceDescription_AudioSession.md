# `AVAudioSessionDataSourceDescription`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
^v _impl;
```

## Properties

```
@property (T@"NSNumber",R) dataSourceID;
@property (T@"NSString",R) dataSourceName;
@property (T@"NSString",R) location;
@property (T@"NSString",R) orientation;
@property (T@"NSArray",R) supportedPolarPatterns;
@property (T@"NSString",R) selectedPolarPattern;
@property (T@"NSString",R) preferredPolarPattern;
```

## Class methods

```
+[AVAudioSessionDataSourceDescription privateCreateArray:portID:sessionID:];
```

## Instance methods

```
-[AVAudioSessionDataSourceDescription preferredPolarPattern];
-[AVAudioSessionDataSourceDescription location];
-[AVAudioSessionDataSourceDescription supportedPolarPatterns];
-[AVAudioSessionDataSourceDescription orientation];
-[AVAudioSessionDataSourceDescription selectedPolarPattern];
-[AVAudioSessionDataSourceDescription initWithSessionID:];
-[AVAudioSessionDataSourceDescription dealloc];
-[AVAudioSessionDataSourceDescription configurePolarPatterns:];
-[AVAudioSessionDataSourceDescription dataSourceID];
-[AVAudioSessionDataSourceDescription privateGetOwningPortID];
-[AVAudioSessionDataSourceDescription dataSourceName];
-[AVAudioSessionDataSourceDescription hash];
-[AVAudioSessionDataSourceDescription description];
-[AVAudioSessionDataSourceDescription privateGetImplementation];
-[AVAudioSessionDataSourceDescription setPreferredPolarPattern:error:];
-[AVAudioSessionDataSourceDescription isEqualToDataSource:];
-[AVAudioSessionDataSourceDescription isEqual:];
-[AVAudioSessionDataSourceDescription initWithRawSourceDescription:andOwningPortID:andSessionID:];
```
