# `_UISceneRegion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSXPCCoding`, `BSXPCSecureCoding`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 11 properties, 19 instance methods, 7 class methods

## Instance variables

```
B _active;
@"NSUUID" _motionBodyIdentifier;
@"NSString" _identifier;
Q _type;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _referenceFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _margins;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_referenceFrame) referenceFrame;
@property (TQ,R,N,V_type) type;
@property (TB,R,N,GisActive,V_active) active;
@property (T{UIEdgeInsets=dddd},R,N,V_margins) margins;
@property (T@"NSUUID",R,C,N,V_motionBodyIdentifier) motionBodyIdentifier;
@property (T@"NSDictionary",R,C,N) metadata;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneRegion supportsBSXPCSecureCoding];
+[_UISceneRegion supportsSecureCoding];
+[_UISceneRegion regionWithIdentifier:referenceFrame:type:active:metadata:];
+[_UISceneRegion regionWithIdentifier:referenceFrame:type:active:];
+[_UISceneRegion regionWithIdentifier:referenceFrame:type:active:margins:motionBodyIdentifier:];
+[_UISceneRegion regionWithIdentifier:referenceFrame:type:];
+[_UISceneRegion regionWithIdentifier:referenceFrame:type:active:margins:metadata:];
```

## Instance methods

```
-[_UISceneRegion debugDescription];
-[_UISceneRegion identifier];
-[_UISceneRegion initWithXPCDictionary:];
-[_UISceneRegion referenceFrame];
-[_UISceneRegion metadata];
-[_UISceneRegion motionBodyIdentifier];
-[_UISceneRegion type];
-[_UISceneRegion margins];
-[_UISceneRegion encodeWithXPCDictionary:];
-[_UISceneRegion encodeWithCoder:];
-[_UISceneRegion hash];
-[_UISceneRegion description];
-[_UISceneRegion initWithCoder:];
-[_UISceneRegion appendDescriptionToStream:];
-[_UISceneRegion encodeWithBSXPCCoder:];
-[_UISceneRegion isActive];
-[_UISceneRegion initWithBSXPCCoder:];
-[_UISceneRegion copyWithZone:];
-[_UISceneRegion isEqual:];
```
