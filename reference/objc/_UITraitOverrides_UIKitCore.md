# `_UITraitOverrides`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITraitOverrideDelegate`, `NSSecureCoding`, `UITraitOverrides`, `UIMutableTraitsInternal`
- 9 instance variables, 29 properties, 79 instance methods, 1 class methods

## Instance variables

```
@"UITraitCollection" _overrides;
@"_UITraitTokenSet" _defaultValueOverrides;
{vector<_UIIdentifiedTraitCollectionTransform, std::allocator<_UIIdentifiedTraitCollectionTransform>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _traitCollectionTransforms;
{vector<_UIIdentifiedChildTraitCollectionTransform, std::allocator<_UIIdentifiedChildTraitCollectionTransform>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _childTraitCollectionTransforms;
{vector<_UIIdentifiedChildTraitOverrides, std::allocator<_UIIdentifiedChildTraitOverrides>>="__begin_"^{?}"__end_"^{?}""{?="__cap_"^{?}}} _childTraitOverrides;
{?="delegateImplementsWillChange"b1} _flags;
@"<_UITraitOverrideDelegate>" _delegate;
@"_UITraitOverrides" _overridesAppliedBefore;
@"_UITraitOverrides" _overridesAppliedAfter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,D,N) userInterfaceIdiom;
@property (Tq,D,N) userInterfaceStyle;
@property (Tq,D,N) layoutDirection;
@property (Td,D,N) displayScale;
@property (Tq,D,N) horizontalSizeClass;
@property (Tq,D,N) verticalSizeClass;
@property (Tq,D,N) forceTouchCapability;
@property (T@"NSString",C,D,N) preferredContentSizeCategory;
@property (Tq,D,N) displayGamut;
@property (Tq,D,N) accessibilityContrast;
@property (Tq,D,N) userInterfaceLevel;
@property (Tq,D,N) legibilityWeight;
@property (Tq,D,N) activeAppearance;
@property (Tq,D,N) toolbarItemPresentationSize;
@property (Tq,N) imageDynamicRange;
@property (Tq,N) sceneCaptureState;
@property (T@"NSString",C,N) typesettingLanguage;
@property (Tq,N) listEnvironment;
@property (Tq,N) tabAccessoryEnvironment;
@property (Tq,N) splitViewControllerLayoutEnvironment;
@property (TB,N) resolvesNaturalAlignmentWithBaseWritingDirection;
@property (TB,N) systemPrefersReducedResourceUsage;
@property (T@"UIColor",R,N) _tintColor;
@property (T@"NSObject",R,N) _environmentWrapper;
@property (Td,N,S_setTypesettingLanguageAwareLineHeightRatio:) _typesettingLanguageAwareLineHeightRatio;
```

## Class methods

```
+[_UITraitOverrides supportsSecureCoding];
```

## Instance methods

```
-[_UITraitOverrides _tintColor];
-[_UITraitOverrides displayGamut];
-[_UITraitOverrides setListEnvironment:];
-[_UITraitOverrides setNSIntegerValue:forTrait:];
-[_UITraitOverrides verticalSizeClass];
-[_UITraitOverrides _description];
-[_UITraitOverrides accessibilityContrast];
-[_UITraitOverrides _traitOverridesWillChange:withApplicator:];
-[_UITraitOverrides _setTintColor:];
-[_UITraitOverrides preferredContentSizeCategory];
-[_UITraitOverrides setDisplayGamut:];
-[_UITraitOverrides setSplitViewControllerLayoutEnvironment:];
-[_UITraitOverrides setDisplayScale:];
-[_UITraitOverrides _environmentWrapper];
-[_UITraitOverrides init];
-[_UITraitOverrides _valueForNSIntegerTraitToken:];
-[_UITraitOverrides setTypesettingLanguage:];
-[_UITraitOverrides setSceneCaptureState:];
-[_UITraitOverrides displayScale];
-[_UITraitOverrides valueForCGFloatTrait:];
-[_UITraitOverrides copy];
-[_UITraitOverrides setLayoutDirection:];
-[_UITraitOverrides _valueForCGFloatTraitToken:];
-[_UITraitOverrides setLegibilityWeight:];
-[_UITraitOverrides activeAppearance];
-[_UITraitOverrides _setCGFloatValue:forTraitToken:];
-[_UITraitOverrides userInterfaceIdiom];
-[_UITraitOverrides listEnvironment];
-[_UITraitOverrides layoutDirection];
-[_UITraitOverrides userInterfaceLevel];
-[_UITraitOverrides setAccessibilityContrast:];
-[_UITraitOverrides setUserInterfaceIdiom:];
-[_UITraitOverrides typesettingLanguage];
-[_UITraitOverrides setResolvesNaturalAlignmentWithBaseWritingDirection:];
-[_UITraitOverrides tabAccessoryEnvironment];
-[_UITraitOverrides _setEnvironmentWrapper:];
-[_UITraitOverrides legibilityWeight];
-[_UITraitOverrides imageDynamicRange];
-[_UITraitOverrides _valueForNSUIntegerTraitToken:];
-[_UITraitOverrides userInterfaceStyle];
-[_UITraitOverrides _setTypesettingLanguageAwareLineHeightRatio:];
-[_UITraitOverrides _setObject:forTraitToken:];
-[_UITraitOverrides setUserInterfaceStyle:];
-[_UITraitOverrides setNSUIntegerValue:forTrait:];
-[_UITraitOverrides setPreferredContentSizeCategory:];
-[_UITraitOverrides setObject:forTrait:];
-[_UITraitOverrides objectForTrait:];
-[_UITraitOverrides setVerticalSizeClass:];
-[_UITraitOverrides encodeWithCoder:];
-[_UITraitOverrides systemPrefersReducedResourceUsage];
-[_UITraitOverrides toolbarItemPresentationSize];
-[_UITraitOverrides hash];
-[_UITraitOverrides description];
-[_UITraitOverrides sceneCaptureState];
-[_UITraitOverrides setToolbarItemPresentationSize:];
-[_UITraitOverrides forceTouchCapability];
-[_UITraitOverrides initWithCoder:];
-[_UITraitOverrides _objectForTraitToken:];
-[_UITraitOverrides _childTraitTransformDidChange];
-[_UITraitOverrides setUserInterfaceLevel:];
-[_UITraitOverrides setSystemPrefersReducedResourceUsage:];
-[_UITraitOverrides setImageDynamicRange:];
-[_UITraitOverrides _typesettingLanguageAwareLineHeightRatio];
-[_UITraitOverrides horizontalSizeClass];
-[_UITraitOverrides setTabAccessoryEnvironment:];
-[_UITraitOverrides setCGFloatValue:forTrait:];
-[_UITraitOverrides isEqual:];
-[_UITraitOverrides valueForNSIntegerTrait:];
-[_UITraitOverrides containsTrait:];
-[_UITraitOverrides resolvesNaturalAlignmentWithBaseWritingDirection];
-[_UITraitOverrides splitViewControllerLayoutEnvironment];
-[_UITraitOverrides setActiveAppearance:];
-[_UITraitOverrides valueForNSUIntegerTrait:];
-[_UITraitOverrides setForceTouchCapability:];
-[_UITraitOverrides setHorizontalSizeClass:];
-[_UITraitOverrides removeTrait:];
-[_UITraitOverrides _setNSUIntegerValue:forTraitToken:];
-[_UITraitOverrides _setNSIntegerValue:forTraitToken:];
-[_UITraitOverrides _traitOverridesDidChange];
```
