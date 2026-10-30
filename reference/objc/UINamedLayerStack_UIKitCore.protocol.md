# `UINamedLayerStack` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) name;
@property (T@"NSArray",R,N) layers;
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N) scale;
@property (T^{CGImage=},R,N) flattenedImage;
@property (T@,?,R,N) radiosityImage;
@property (T{CGSize=dd},?,R,N) radiosityImageScale;
@property (TB,?,R,N) flatImageContainsCornerRadius;
```

## Instance methods

```
-[UINamedLayerStack layers];
-[UINamedLayerStack size];
-[UINamedLayerStack scale];
-[UINamedLayerStack name];
-[UINamedLayerStack flattenedImage];
-[UINamedLayerStack flatImageContainsCornerRadius];
-[UINamedLayerStack radiosityImage];
-[UINamedLayerStack radiosityImageScale];
```
