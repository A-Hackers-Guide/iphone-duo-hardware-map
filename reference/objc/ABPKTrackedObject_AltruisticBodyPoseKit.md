# `ABPKTrackedObject`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _objectID;
@"NSString" _category;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundingBox;
Q _confidence;
```

## Properties

```
@property (TQ,R,N,V_objectID) objectID;
@property (T@"NSString",R,N,V_category) category;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_boundingBox) boundingBox;
@property (TQ,R,N,V_confidence) confidence;
```

## Instance methods

```
-[ABPKTrackedObject category];
-[ABPKTrackedObject boundingBox];
-[ABPKTrackedObject objectID];
-[ABPKTrackedObject confidence];
-[ABPKTrackedObject initWithObjectID:category:boundingBox:confidence:];
```
