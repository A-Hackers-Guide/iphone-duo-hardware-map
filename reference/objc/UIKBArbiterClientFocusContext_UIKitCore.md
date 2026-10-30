# `UIKBArbiterClientFocusContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`
- 3 instance variables, 7 properties, 14 instance methods, 4 class methods

## Instance variables

```
I _contextID;
@"FBSSceneIdentityToken" _sceneIdentity;
@"FBSSceneIdentityToken" _layeringSceneIdentity;
```

## Properties

```
@property (TI,N,V_contextID) contextID;
@property (T@"FBSSceneIdentityToken",&,N,V_sceneIdentity) sceneIdentity;
@property (T@"FBSSceneIdentityToken",&,N,V_layeringSceneIdentity) layeringSceneIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBArbiterClientFocusContext supportsBSXPCSecureCoding];
+[UIKBArbiterClientFocusContext supportsSecureCoding];
+[UIKBArbiterClientFocusContext focusContextForSceneIdentity:window:];
+[UIKBArbiterClientFocusContext focusContextForSceneIdentity:contextID:];
```

## Instance methods

```
-[UIKBArbiterClientFocusContext descriptionForLog];
-[UIKBArbiterClientFocusContext setContextID:];
-[UIKBArbiterClientFocusContext setSceneIdentity:];
-[UIKBArbiterClientFocusContext sceneIdentity];
-[UIKBArbiterClientFocusContext setLayeringSceneIdentity:];
-[UIKBArbiterClientFocusContext encodeWithCoder:];
-[UIKBArbiterClientFocusContext description];
-[UIKBArbiterClientFocusContext initWithCoder:];
-[UIKBArbiterClientFocusContext layeringSceneIdentity];
-[UIKBArbiterClientFocusContext encodeWithBSXPCCoder:];
-[UIKBArbiterClientFocusContext contextID];
-[UIKBArbiterClientFocusContext initWithBSXPCCoder:];
-[UIKBArbiterClientFocusContext copyWithZone:];
-[UIKBArbiterClientFocusContext isEqual:];
```
