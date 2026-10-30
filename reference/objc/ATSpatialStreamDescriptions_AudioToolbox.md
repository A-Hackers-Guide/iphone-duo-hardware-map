# `ATSpatialStreamDescriptions`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _type;
@"AVAudioFormat" _flatFormat;
@"AVAudioFormat" _streamFormat;
@"NSMutableArray" _streamParameters;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (T@"AVAudioFormat",R,N,V_flatFormat) flatFormat;
@property (T@"AVAudioFormat",R,N,V_streamFormat) streamFormat;
@property (T@"NSArray",R,N) streamParameters;
```

## Instance methods

```
-[ATSpatialStreamDescriptions init];
-[ATSpatialStreamDescriptions type];
-[ATSpatialStreamDescriptions description];
-[ATSpatialStreamDescriptions flatFormat];
-[ATSpatialStreamDescriptions initWithFlatIOFormat:type:];
-[ATSpatialStreamDescriptions streamFormat];
-[ATSpatialStreamDescriptions streamParameters];
```
