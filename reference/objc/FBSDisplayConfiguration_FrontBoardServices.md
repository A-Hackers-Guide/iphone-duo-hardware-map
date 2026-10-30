# `FBSDisplayConfiguration`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 24 instance variables, 32 properties, 66 instance methods, 2 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _nativeBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _bounds;
{CGSize="width"d"height"d} _safeOverscanRatio;
{CGSize="width"d"height"d} _pixelSize;
@"FBSDisplayPixelDensity" _pixelDensity;
d _latency;
@"FBSDisplayIdentity" _identity;
@"NSString" _hardwareIdentifier;
@"NSString" _name;
@"NSString" _deviceName;
@"FBSDisplayMode" _currentMode;
@"FBSDisplayMode" _preferredMode;
@"NSSet" _otherModes;
@"NSSet" _availableModes;
@"CADisplay" _immutableCADisplay;
@"CADisplay" _caDisplay;
q _tags;
q _overscanCompensation;
I _noEqual_seed;
i _pid;
B _cloningSupported;
B _overscanned;
B _noEqual_comparable;
@"FBSDisplayConfiguration" _noEqual_originatingConfiguration;
```

## Properties

```
@property (TI,R,N,V_noEqual_seed) seed;
@property (Tq,R,N,V_tags) tags;
@property (TB,R,N,GisUIKitMainLike) UIKitMainLike;
@property (T@"FBSDisplayConfiguration",R,C,N,V_noEqual_originatingConfiguration) originatingConfiguration;
@property (T@"FBSDisplayIdentity",R,C,N,V_identity) identity;
@property (TB,R,N,GisMainDisplay) mainDisplay;
@property (TB,R,N,GisExternal) external;
@property (TB,R,N,GisCarDisplay) carDisplay;
@property (TB,R,N,GisCarInstrumentsDisplay) carInstrumentsDisplay;
@property (T@"NSString",R,C,N,V_hardwareIdentifier) hardwareIdentifier;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSString",R,C,N,V_deviceName) deviceName;
@property (T@"FBSDisplayMode",R,C,N,V_currentMode) currentMode;
@property (T@"FBSDisplayMode",R,C,N) preferredMode;
@property (T@"NSSet",R,C,N,V_availableModes) availableModes;
@property (TB,R,N,GisCloningSupported,V_cloningSupported) cloningSupported;
@property (TB,R,N,GisOverscanned,V_overscanned) overscanned;
@property (Tq,R,N,V_overscanCompensation) overscanCompensation;
@property (T{CGSize=dd},R,N,V_safeOverscanRatio) safeOverscanRatio;
@property (Td,R,N) nativeOrientation;
@property (T{CGSize=dd},R,N,V_pixelSize) pixelSize;
@property (Td,R,N) pointScale;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds) bounds;
@property (T{CGPoint=dd},R,N) renderingCenter;
@property (T@"FBSDisplayPixelDensity",R,C,N,V_pixelDensity) pixelDensity;
@property (Td,R,N) refreshRate;
@property (Tq,R,N) colorGamut;
@property (Td,R,N,V_latency) latency;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayConfiguration supportsSecureCoding];
+[FBSDisplayConfiguration _virtualDisplayConfigurationWithIdentifier:];
```

## Instance methods

```
-[FBSDisplayConfiguration isOverscanned];
-[FBSDisplayConfiguration seed];
-[FBSDisplayConfiguration latency];
-[FBSDisplayConfiguration isExternal];
-[FBSDisplayConfiguration hardwareIdentifier];
-[FBSDisplayConfiguration currentMode];
-[FBSDisplayConfiguration tags];
-[FBSDisplayConfiguration preferredMode];
-[FBSDisplayConfiguration nativeOrientation];
-[FBSDisplayConfiguration refreshRate];
-[FBSDisplayConfiguration availableModes];
-[FBSDisplayConfiguration succinctDescriptionBuilder];
-[FBSDisplayConfiguration isCloningSupported];
-[FBSDisplayConfiguration init];
-[FBSDisplayConfiguration isCarDisplay];
-[FBSDisplayConfiguration isVirtualized];
-[FBSDisplayConfiguration initWithXPCDictionary:];
-[FBSDisplayConfiguration pointScale];
-[FBSDisplayConfiguration isUIKitMainLike];
-[FBSDisplayConfiguration descriptionWithMultilinePrefix:];
-[FBSDisplayConfiguration uniqueIdentifier];
-[FBSDisplayConfiguration _nativeBounds];
-[FBSDisplayConfiguration pixelSize];
-[FBSDisplayConfiguration succinctDescription];
-[FBSDisplayConfiguration scale];
-[FBSDisplayConfiguration colorGamut];
-[FBSDisplayConfiguration initWithCADisplay:];
-[FBSDisplayConfiguration isMainRootDisplay];
-[FBSDisplayConfiguration type];
-[FBSDisplayConfiguration encodeWithXPCDictionary:];
-[FBSDisplayConfiguration isCarInstrumentsDisplay];
-[FBSDisplayConfiguration encodeWithCoder:];
-[FBSDisplayConfiguration expectsSecureRendering];
-[FBSDisplayConfiguration hash];
-[FBSDisplayConfiguration identity];
-[FBSDisplayConfiguration bounds];
-[FBSDisplayConfiguration caDisplay];
-[FBSDisplayConfiguration isMainDisplay];
-[FBSDisplayConfiguration description];
-[FBSDisplayConfiguration initWithCoder:];
-[FBSDisplayConfiguration copyWithZone:];
-[FBSDisplayConfiguration isEqual:];
-[FBSDisplayConfiguration deviceName];
-[FBSDisplayConfiguration name];
-[FBSDisplayConfiguration descriptionBuilderWithMultilinePrefix:];
-[FBSDisplayConfiguration CADisplay];
-[FBSDisplayConfiguration renderingCenter];
-[FBSDisplayConfiguration _nameForDisplayType];
-[FBSDisplayConfiguration overscanCompensation];
-[FBSDisplayConfiguration safeOverscanRatio];
-[FBSDisplayConfiguration _nativeRotation];
-[FBSDisplayConfiguration isHiddenDisplay];
-[FBSDisplayConfiguration _initWithIdentity:hardwareIdentifier:name:deviceName:seed:comparable:tags:currentMode:preferredMode:otherModes:cloningSupported:overscanned:overscanCompensation:safeOverscanRatio:pixelSize:nativeBounds:bounds:pixelDensity:latency:originatingConfiguration:validityCheck:];
-[FBSDisplayConfiguration _initWithImmutableDisplay:originalDisplay:isMainDisplay:assertIfInvalid:];
-[FBSDisplayConfiguration copyForSecureRendering];
-[FBSDisplayConfiguration copyWithOverrideBounds:];
-[FBSDisplayConfiguration copyWithOverrideMode:];
-[FBSDisplayConfiguration copyWithOverrideMode:pixelSize:nativeBounds:];
-[FBSDisplayConfiguration copyWithUniqueIdentifier:];
-[FBSDisplayConfiguration immutableCADisplay];
-[FBSDisplayConfiguration laterConfiguration:];
-[FBSDisplayConfiguration nativeCenter];
-[FBSDisplayConfiguration originatingConfiguration];
-[FBSDisplayConfiguration pixelDensity];
-[FBSDisplayConfiguration supportsExtendedColor];
-[FBSDisplayConfiguration wantsConnectionDebouncing];
```
