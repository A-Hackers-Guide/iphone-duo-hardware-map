# `UIPointerRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContentEffectKey`, `NSCopying`
- 5 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"<NSObject>" _identifier;
Q _latchingAxes;
Q _generationID;
@"UIView" _referenceView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rect;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect) rect;
@property (T@"<NSObject>",&,N,V_identifier) identifier;
@property (TQ,N,V_generationID) generationID;
@property (TB,R,N) _isLatching;
@property (T@"UIView",W,N,V_referenceView) referenceView;
@property (TQ,N,V_latchingAxes) latchingAxes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPointerRegion regionWithRect:identifier:];
```

## Instance methods

```
-[UIPointerRegion setGenerationID:];
-[UIPointerRegion identifier];
-[UIPointerRegion latchingAxes];
-[UIPointerRegion generationID];
-[UIPointerRegion setLatchingAxes:];
-[UIPointerRegion setIdentifier:];
-[UIPointerRegion _isLatching];
-[UIPointerRegion rect];
-[UIPointerRegion setRect:];
-[UIPointerRegion setReferenceView:];
-[UIPointerRegion hash];
-[UIPointerRegion description];
-[UIPointerRegion copyWithZone:];
-[UIPointerRegion isEqual:];
-[UIPointerRegion referenceView];
```
