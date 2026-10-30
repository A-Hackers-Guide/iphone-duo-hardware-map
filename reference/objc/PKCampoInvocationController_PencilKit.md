# `PKCampoInvocationController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICampoLightweightControllerDelegate`
- 2 instance variables, 6 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"_UICampoLightweightController" _campoLightweightController;
@"<PKCampoInvocationControllerDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N) canInvokeCampo;
@property (T@"<PKCampoInvocationControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKCampoInvocationController isCampoSupportedForWritingTools];
```

## Instance methods

```
-[PKCampoInvocationController dealloc];
-[PKCampoInvocationController setDelegate:];
-[PKCampoInvocationController delegate];
-[PKCampoInvocationController campoLightweightController:didChangeFromState:toState:];
-[PKCampoInvocationController campoLightweightControllerDidDismiss:];
-[PKCampoInvocationController canInvokeCampo];
-[PKCampoInvocationController dismissCampoAnimated:];
-[PKCampoInvocationController invokeCampoWithPresentingViewController:configuration:context:animated:];
```
