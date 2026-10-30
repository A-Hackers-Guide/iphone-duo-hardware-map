# `SRFrameStore`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 7 instance variables, 0 properties, 2 instance methods, 1 class methods

## Instance variables

```
I _datastoreVersion;
@"SRMemoryMapping" _frames;
@"SRMemoryMapping" _header;
Q _permission;
@"NSString" _segmentName;
d _lastAbsoluteTimestamp;
@"NSFileHandle" _backingFile;
```

## Class methods

```
+[SRFrameStore initialize];
```

## Instance methods

```
-[SRFrameStore dealloc];
-[SRFrameStore countByEnumeratingWithState:objects:count:];
```
