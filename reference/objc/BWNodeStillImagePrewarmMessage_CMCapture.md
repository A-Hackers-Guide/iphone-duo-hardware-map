# `BWNodeStillImagePrewarmMessage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNodeMessage`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageSettings" _stillImageSettings;
@"BWPrewarmResourceConfiguration" _resourceConfig;
```

## Properties

```
@property (T@"BWStillImageSettings",R) stillImageSettings;
@property (T@"BWPrewarmResourceConfiguration",R,V_resourceConfig) resourceConfig;
```

## Class methods

```
+[BWNodeStillImagePrewarmMessage newMessageWithStillImageSettings:resourceConfig:];
```

## Instance methods

```
-[BWNodeStillImagePrewarmMessage stillImageSettings];
-[BWNodeStillImagePrewarmMessage dealloc];
-[BWNodeStillImagePrewarmMessage _initWithStillImageSettings:resourceConfig:];
-[BWNodeStillImagePrewarmMessage resourceConfig];
```
