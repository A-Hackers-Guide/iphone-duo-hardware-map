# `ATSpatialStreamParameters`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _identifier;
@"AVAudioFormat" _format;
```

## Properties

```
@property (TB,R,N,GisEnabled) enabled;
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (T@"AVAudioFormat",R,N,V_format) format;
```

## Instance methods

```
-[ATSpatialStreamParameters identifier];
-[ATSpatialStreamParameters init];
-[ATSpatialStreamParameters isEnabled];
-[ATSpatialStreamParameters hash];
-[ATSpatialStreamParameters description];
-[ATSpatialStreamParameters isEqual:];
-[ATSpatialStreamParameters format];
-[ATSpatialStreamParameters disableStream];
-[ATSpatialStreamParameters enableStreamWithIdentifier:error:];
-[ATSpatialStreamParameters initInternalWithFormat:];
```
