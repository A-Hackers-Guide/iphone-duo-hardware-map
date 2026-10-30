# `_MTLFunctionLogDebugLocation`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLFunctionLogDebugLocation`
- 2 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"MTLDebugLocation" _debugLocation;
@"NSURL" _URL;
```

## Properties

```
@property (T@"NSString",R) functionName;
@property (T@"NSURL",R,V_URL) URL;
@property (TQ,R) line;
@property (TQ,R) column;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLFunctionLogDebugLocation functionName];
-[_MTLFunctionLogDebugLocation dealloc];
-[_MTLFunctionLogDebugLocation description];
-[_MTLFunctionLogDebugLocation URL];
-[_MTLFunctionLogDebugLocation column];
-[_MTLFunctionLogDebugLocation line];
-[_MTLFunctionLogDebugLocation initWithDebugLocation:];
```
