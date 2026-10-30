# `ICDocCamImageQuad` (protocol)

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},R) topLeft;
@property (T{CGPoint=dd},R) topRight;
@property (T{CGPoint=dd},R) bottomLeft;
@property (T{CGPoint=dd},R) bottomRight;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R) boundingBox;
```

## Instance methods

```
-[ICDocCamImageQuad topRight];
-[ICDocCamImageQuad bottomLeft];
-[ICDocCamImageQuad boundingBox];
-[ICDocCamImageQuad bottomRight];
-[ICDocCamImageQuad topLeft];
```
