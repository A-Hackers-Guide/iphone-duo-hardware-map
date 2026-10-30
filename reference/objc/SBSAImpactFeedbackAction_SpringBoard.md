# `SBSAImpactFeedbackAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAActionRepresenting`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _prepareOnly;
@"NSArray" _reasons;
q _impactFeedbackStyle;
```

## Properties

```
@property (Tq,R,N,V_impactFeedbackStyle) impactFeedbackStyle;
@property (TB,R,N,V_prepareOnly) prepareOnly;
@property (T@"NSArray",R,C,N,V_reasons) reasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAImpactFeedbackAction initialize];
```

## Instance methods

```
-[SBSAImpactFeedbackAction reasons];
-[SBSAImpactFeedbackAction encodeWithCoder:];
-[SBSAImpactFeedbackAction hash];
-[SBSAImpactFeedbackAction description];
-[SBSAImpactFeedbackAction copyWithZone:];
-[SBSAImpactFeedbackAction isEqual:];
-[SBSAImpactFeedbackAction membersForCoder];
-[SBSAImpactFeedbackAction impactFeedbackStyle];
-[SBSAImpactFeedbackAction initWithImpactFeedbackStyle:prepareOnly:reasons:];
-[SBSAImpactFeedbackAction prepareOnly];
```
