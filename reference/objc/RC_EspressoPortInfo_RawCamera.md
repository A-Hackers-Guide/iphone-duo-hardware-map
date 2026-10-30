# `RC_EspressoPortInfo`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
B _isInput;
Q _width;
Q _height;
Q _depth;
@"IOSurface" _surface;
@? _surfaceReleaseBlock;
```

## Properties

```
@property (T@"NSString",R,V_name) name;
@property (TB,R,V_isInput) isInput;
@property (TQ,R,V_width) width;
@property (TQ,R,V_height) height;
@property (TQ,R,V_depth) depth;
@property (T@"IOSurface",R,V_surface) surface;
@property (T@?,C,N,V_surfaceReleaseBlock) surfaceReleaseBlock;
```

## Instance methods

```
-[RC_EspressoPortInfo depth];
-[RC_EspressoPortInfo isInput];
-[RC_EspressoPortInfo surface];
-[RC_EspressoPortInfo dealloc];
-[RC_EspressoPortInfo width];
-[RC_EspressoPortInfo name];
-[RC_EspressoPortInfo height];
-[RC_EspressoPortInfo initWithName:isInput:width:height:depth:surface:];
-[RC_EspressoPortInfo setSurfaceReleaseBlock:];
-[RC_EspressoPortInfo surfaceReleaseBlock];
```
