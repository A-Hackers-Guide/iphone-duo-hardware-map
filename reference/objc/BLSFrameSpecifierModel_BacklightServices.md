# `BLSFrameSpecifierModel`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _specifiers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _stateHandler;
```

## Properties

```
@property (T@"NSArray",R) specifiers;
@property (TQ,R) specifierCount;
```

## Instance methods

```
-[BLSFrameSpecifierModel debugDescription];
-[BLSFrameSpecifierModel init];
-[BLSFrameSpecifierModel dealloc];
-[BLSFrameSpecifierModel description];
-[BLSFrameSpecifierModel addSpecifiers:];
-[BLSFrameSpecifierModel specifierAtPresentationDate:];
-[BLSFrameSpecifierModel specifiers];
-[BLSFrameSpecifierModel specifierCount];
-[BLSFrameSpecifierModel purgeAllButOneSpecifiersBeforeDate:];
-[BLSFrameSpecifierModel purgeAllSpecifiersOnOrAfterDate:];
```
