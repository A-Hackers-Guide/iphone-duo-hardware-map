# `UIPointerStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIHoverStyle`
- Protocols: `_UIContentEffectDescriptor`, `NSCopying`
- 8 instance variables, 16 properties, 32 instance methods, 6 class methods

## Instance variables

```
B _determineScaleAutomatically;
B _suppressesMirroring;
@"NSArray" _accessories;
q _type;
Q _options;
Q _constrainedAxes;
@"UIPointerEffect" _pointerEffect;
@"UIPointerShape" _pointerShape;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (TQ,N,V_options) options;
@property (TQ,N,V_constrainedAxes) constrainedAxes;
@property (T@"UIPointerEffect",&,N,V_pointerEffect) pointerEffect;
@property (T@"UIPointerShape",&,N,V_pointerShape) pointerShape;
@property (Td,R,N) contentScale;
@property (TB,R,N) pointerUnderlapsContent;
@property (TB,R,N) pointerMergesWithContent;
@property (TB,N,V_suppressesMirroring) _suppressesMirroring;
@property (T@"NSArray",C,N,V_accessories) accessories;
@property (T@"UITargetedPreview",R,N) targetedPreview;
@property (T@"NSArray",R,N) compatibleDescriptors;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPointerStyle styleWithShape:constrainedAxes:];
+[UIPointerStyle _makeStyleWithHoverStyle:view:convertAutomatic:];
+[UIPointerStyle _systemPointerStyle];
+[UIPointerStyle hiddenPointerStyle];
+[UIPointerStyle styleWithEffect:shape:];
+[UIPointerStyle systemPointerStyle];
```

## Instance methods

```
-[UIPointerStyle setOptions:];
-[UIPointerStyle accessories];
-[UIPointerStyle effect];
-[UIPointerStyle setType:];
-[UIPointerStyle type];
-[UIPointerStyle contentScale];
-[UIPointerStyle setAccessories:];
-[UIPointerStyle setEffect:];
-[UIPointerStyle hash];
-[UIPointerStyle description];
-[UIPointerStyle options];
-[UIPointerStyle copyWithZone:];
-[UIPointerStyle isEqual:];
-[UIPointerStyle _pointerSlipMappedToRegionSize:];
-[UIPointerStyle _contentSlipMappedToRegionSize:];
-[UIPointerStyle constrainedAxes];
-[UIPointerStyle targetedPreview];
-[UIPointerStyle _adaptForNonSystemEffectSupportingEnvironment];
-[UIPointerStyle _contentSlipFactor];
-[UIPointerStyle _pointerIntensityForMaterialLuminance:];
-[UIPointerStyle _pointerSlipFactor];
-[UIPointerStyle _suppressesMirroring];
-[UIPointerStyle canTransitionInPlaceToEffectWithDescriptor:];
-[UIPointerStyle compatibleDescriptors];
-[UIPointerStyle pointerEffect];
-[UIPointerStyle pointerMergesWithContent];
-[UIPointerStyle pointerShape];
-[UIPointerStyle pointerUnderlapsContent];
-[UIPointerStyle setConstrainedAxes:];
-[UIPointerStyle setPointerEffect:];
-[UIPointerStyle setPointerShape:];
-[UIPointerStyle set_suppressesMirroring:];
```
