# `FBSDisplayConfigurationBuilder`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"FBSDisplayConfiguration" _configuration;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSString" _lock_uniqueIdentifier;
@"FBSDisplayMode" _lock_currentMode;
@"FBSDisplayMode" _lock_preferredMode;
@"NSSet" _lock_otherModes;
{CGSize="width"d"height"d} _lock_pixelSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lock_nativeBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lock_bounds;
B _lock_geometrySet;
@"FBSDisplayPixelDensity" _lock_pixelDensity;
B _lock_pixelDensitySet;
B _lock_secure;
B _lock_mainLike;
B _lock_cloningSupported;
B _lock_cloningSet;
q _lock_displayType;
B _lock_displayTypeSet;
q _lock_overscanCompensation;
{CGSize="width"d"height"d} _lock_safeOverscanRatio;
B _lock_overscanned;
B _lock_overscanSet;
```

## Instance methods

```
-[FBSDisplayConfigurationBuilder buildWithError:];
-[FBSDisplayConfigurationBuilder setDisplayType:];
-[FBSDisplayConfigurationBuilder init];
-[FBSDisplayConfigurationBuilder setUniqueIdentifier:];
-[FBSDisplayConfigurationBuilder initWithConfiguration:];
-[FBSDisplayConfigurationBuilder _lock_sanitizedModeForMode:];
-[FBSDisplayConfigurationBuilder buildConfigurationWithError:];
-[FBSDisplayConfigurationBuilder setCloningNotSupported];
-[FBSDisplayConfigurationBuilder setCloningSupported:];
-[FBSDisplayConfigurationBuilder setCurrentMode:preferredMode:otherModes:];
-[FBSDisplayConfigurationBuilder setExpectsSecureRendering];
-[FBSDisplayConfigurationBuilder setOverscanned:compensation:safeRatio:];
-[FBSDisplayConfigurationBuilder setPixelDensity:];
-[FBSDisplayConfigurationBuilder setPixelSize:nativeBounds:bounds:];
-[FBSDisplayConfigurationBuilder setUIKitMainLike];
```
