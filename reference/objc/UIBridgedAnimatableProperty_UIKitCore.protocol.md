# `UIBridgedAnimatableProperty` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@,&,N) value;
@property (T@,&,N) presentationValue;
@property (T@,&,N) velocity;
@property (T@"UIView",W,N) view;
@property (TB,R,N) isInvalidated;
@property (T@,&,N) transformer;
@property (TB,N) isVelocityUsableForVFD;
```

## Instance methods

```
-[UIBridgedAnimatableProperty presentationValue];
-[UIBridgedAnimatableProperty value];
-[UIBridgedAnimatableProperty setView:];
-[UIBridgedAnimatableProperty velocity];
-[UIBridgedAnimatableProperty isInvalidated];
-[UIBridgedAnimatableProperty view];
-[UIBridgedAnimatableProperty setValue:];
-[UIBridgedAnimatableProperty transformer];
-[UIBridgedAnimatableProperty setTransformer:];
-[UIBridgedAnimatableProperty setVelocity:];
-[UIBridgedAnimatableProperty velocityTarget:];
-[UIBridgedAnimatableProperty invalidateAndStopImmediately:];
-[UIBridgedAnimatableProperty isVelocityUsableForVFD];
-[UIBridgedAnimatableProperty setIsVelocityUsableForVFD:];
-[UIBridgedAnimatableProperty setPresentationValue:];
-[UIBridgedAnimatableProperty setVelocity:target:];
```
