# `UIAttachmentBehavior`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIDynamicBehavior`
- 15 instance variables, 8 properties, 28 instance methods, 6 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _anchorPoint;
{CGPoint="x"d"y"d} _anchorPointA;
{CGPoint="x"d"y"d} _anchorPointB;
@"PKExtendedPhysicsBody" _anchorBody;
@"PKPhysicsJoint" _joint;
d _damping;
d _frequency;
d _length;
{CGVector="dx"d"dy"d} _axis;
Q _attachmentType;
q _type;
{?="dampingSet"b1"frequencySet"b1"lengthSet"b1"rangeSet"b1"frictionTorqueSet"b1"isRevolute"b1} _stateFlags;
q _attachedBehaviorType;
d _frictionTorque;
{?="minimum"d"maximum"d} _attachmentRange;
```

## Properties

```
@property (T@"NSArray",R,C,N) items;
@property (Tq,R,N,V_attachedBehaviorType) attachedBehaviorType;
@property (T{CGPoint=dd},N) anchorPoint;
@property (Td,N) length;
@property (Td,N) damping;
@property (Td,N) frequency;
@property (Td,N,V_frictionTorque) frictionTorque;
@property (T{?=dd},N,V_attachmentRange) attachmentRange;
```

## Class methods

```
+[UIAttachmentBehavior _isPrimitiveBehavior];
+[UIAttachmentBehavior fixedAttachmentWithItem:attachedToItem:attachmentAnchor:];
+[UIAttachmentBehavior limitAttachmentWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:];
+[UIAttachmentBehavior pinAttachmentWithItem:attachedToItem:attachmentAnchor:];
+[UIAttachmentBehavior slidingAttachmentWithItem:attachedToItem:attachmentAnchor:axisOfTranslation:];
+[UIAttachmentBehavior slidingAttachmentWithItem:attachmentAnchor:axisOfTranslation:];
```

## Instance methods

```
-[UIAttachmentBehavior setDamping:];
-[UIAttachmentBehavior frequency];
-[UIAttachmentBehavior init];
-[UIAttachmentBehavior anchorPoint];
-[UIAttachmentBehavior damping];
-[UIAttachmentBehavior items];
-[UIAttachmentBehavior length];
-[UIAttachmentBehavior setFrequency:];
-[UIAttachmentBehavior type];
-[UIAttachmentBehavior description];
-[UIAttachmentBehavior setLength:];
-[UIAttachmentBehavior setAnchorPoint:];
-[UIAttachmentBehavior attachmentRange];
-[UIAttachmentBehavior _associate];
-[UIAttachmentBehavior _changedParameter];
-[UIAttachmentBehavior _dissociate];
-[UIAttachmentBehavior _reevaluateJoint];
-[UIAttachmentBehavior _updateJointWithRange:];
-[UIAttachmentBehavior attachedBehaviorType];
-[UIAttachmentBehavior frictionTorque];
-[UIAttachmentBehavior initWithItem:attachedToAnchor:];
-[UIAttachmentBehavior initWithItem:attachedToItem:];
-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToAnchor:];
-[UIAttachmentBehavior initWithItem:offsetFromCenter:attachedToItem:offsetFromCenter:];
-[UIAttachmentBehavior initWithItem:point:attachedToAnchor:];
-[UIAttachmentBehavior initWithItem:point:attachedToItem:point:];
-[UIAttachmentBehavior setAttachmentRange:];
-[UIAttachmentBehavior setFrictionTorque:];
```
