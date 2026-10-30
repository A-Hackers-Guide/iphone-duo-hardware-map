# `_UISpringParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 2 class methods

## Instance variables

```
d __dampingRatio;
d __response;
```

## Properties

```
@property (Td,R,N,V__dampingRatio) _dampingRatio;
@property (Td,R,N,V__response) _response;
```

## Class methods

```
+[_UISpringParameters supportsSecureCoding];
+[_UISpringParameters parametersWithDampingRatio:response:];
```

## Instance methods

```
-[_UISpringParameters initWithDampingRatio:response:];
-[_UISpringParameters encodeWithCoder:];
-[_UISpringParameters description];
-[_UISpringParameters initWithCoder:];
-[_UISpringParameters copyWithZone:];
-[_UISpringParameters isEqual:];
-[_UISpringParameters _dampingRatio];
-[_UISpringParameters _response];
```
