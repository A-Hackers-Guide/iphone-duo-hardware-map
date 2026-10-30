# `CADisplayProperties`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
I _mask;
@"CADisplayMode" _currentMode;
@"NSString" _overscanAdjustment;
B _dmrrEnabled;
I _connectionSeed;
{CGSize="width"d"height"d} _logicalScale;
I _pointScale;
B _forceFixedRateLinks;
```

## Properties

```
@property (TI,N) updateMask;
@property (TB,N) dmrrEnabled;
@property (TB,N) forceFixedRateLinks;
@property (T@"CADisplayMode",&,N) currentMode;
@property (T@"NSString",C,N) overscanAdjustment;
@property (T{CGSize=dd},N) logicalScale;
@property (TQ,N) pointScale;
@property (TI,N) connectionSeed;
```

## Instance methods

```
-[CADisplayProperties connectionSeed];
-[CADisplayProperties currentMode];
-[CADisplayProperties setOverscanAdjustment:];
-[CADisplayProperties overscanAdjustment];
-[CADisplayProperties init];
-[CADisplayProperties pointScale];
-[CADisplayProperties logicalScale];
-[CADisplayProperties dealloc];
-[CADisplayProperties setCurrentMode:];
-[CADisplayProperties setDmrrEnabled:];
-[CADisplayProperties clearUpdateMask];
-[CADisplayProperties dmrrEnabled];
-[CADisplayProperties forceFixedRateLinks];
-[CADisplayProperties needsUpdateForField:];
-[CADisplayProperties setConnectionSeed:];
-[CADisplayProperties setForceFixedRateLinks:];
-[CADisplayProperties setLogicalScale:];
-[CADisplayProperties setPointScale:];
-[CADisplayProperties setUpdateMask:];
-[CADisplayProperties updateMask];
```
