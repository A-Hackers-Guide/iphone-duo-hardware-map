# `_UITextKitTextPosition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITextPosition`
- 3 instance variables, 3 properties, 7 instance methods, 3 class methods

## Instance variables

```
q _offset;
q _affinity;
@"<NSTextLocation>" _location;
```

## Properties

```
@property (Tq,R,N,V_offset) offset;
@property (Tq,R,N,V_affinity) affinity;
@property (T@"<NSTextLocation>",R,N,V_location) location;
```

## Class methods

```
+[_UITextKitTextPosition positionWithOffset:];
+[_UITextKitTextPosition positionWithTextContentManager:location:affinity:];
+[_UITextKitTextPosition positionWithOffset:affinity:];
```

## Instance methods

```
-[_UITextKitTextPosition affinity];
-[_UITextKitTextPosition compare:];
-[_UITextKitTextPosition init];
-[_UITextKitTextPosition location];
-[_UITextKitTextPosition description];
-[_UITextKitTextPosition isEqual:];
-[_UITextKitTextPosition offset];
```
