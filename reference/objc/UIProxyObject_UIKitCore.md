# `UIProxyObject`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 1 instance variables, 0 properties, 4 instance methods, 5 class methods

## Instance variables

```
@"NSString" proxiedObjectIdentifier;
```

## Class methods

```
+[UIProxyObject addMappingFromIdentifier:toObject:forCoder:];
+[UIProxyObject addMappings:forCoder:];
+[UIProxyObject mappedObjectForCoder:withIdentifier:];
+[UIProxyObject proxyDecodingMap];
+[UIProxyObject removeMappingsForCoder:];
```

## Instance methods

```
-[UIProxyObject encodeWithCoder:];
-[UIProxyObject initWithCoder:];
-[UIProxyObject proxiedObjectIdentifier];
-[UIProxyObject setProxiedObjectIdentifier:];
```
