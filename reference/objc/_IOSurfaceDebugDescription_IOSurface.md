# `_IOSurfaceDebugDescription`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOSurfaceDebugDescription`
- 3 instance variables, 12 properties, 15 instance methods, 0 class methods

## Instance variables

```
{?="clientAddress"Q"surfaceID"I"pixelFormat"I"retainCount"I"yCbCrMatrix"I"cacheMode"I"mapCacheAttribute"I"purgeableState"I"purgeableStateAPI"I"allocOffset"Q"allocSize"Q"isGlobal"C"isAllocated"C"isWired"C"pad"C"parentSurfaceID"I"detachModeCode"Q"initDetachModeCodeTime"Q"protectionOptions"Q"residentSize"Q"dirtySize"Q"traceID"Q"memDescID"Q} _basicInfo;
{?="offset"Q"width"Q"height"Q"bytesPerRow"Q"bytesPerElement"I"elementWidth"I"elementHeight"I} _layoutInfo;
@"NSString" _name;
```

## Properties

```
@property (TQ,R) virtualAddress;
@property (TQ,R) allocationSize;
@property (TI,R) surfaceID;
@property (TI,R) pixelFormat;
@property (T@"NSString",R) pixelFormatString;
@property (TQ,R) width;
@property (TQ,R) height;
@property (TQ,R) residentSize;
@property (TQ,R) dirtySize;
@property (T@"NSString",R) name;
@property (TQ,R) traceID;
@property (TB,R) isWired;
```

## Instance methods

```
-[_IOSurfaceDebugDescription surfaceID];
-[_IOSurfaceDebugDescription allocationSize];
-[_IOSurfaceDebugDescription dealloc];
-[_IOSurfaceDebugDescription description];
-[_IOSurfaceDebugDescription pixelFormat];
-[_IOSurfaceDebugDescription width];
-[_IOSurfaceDebugDescription virtualAddress];
-[_IOSurfaceDebugDescription traceID];
-[_IOSurfaceDebugDescription name];
-[_IOSurfaceDebugDescription height];
-[_IOSurfaceDebugDescription isWired];
-[_IOSurfaceDebugDescription dirtySize];
-[_IOSurfaceDebugDescription residentSize];
-[_IOSurfaceDebugDescription pixelFormatString];
-[_IOSurfaceDebugDescription initWithBasicInfo:layoutInfo:name:];
```
