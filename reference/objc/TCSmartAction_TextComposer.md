# `TCSmartAction`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"<TCSmartActionMetadata>" _actionMetadata;
```

## Properties

```
@property (T@"NSString",R,N) actionType;
@property (T@"<TCSmartActionMetadata>",R,C,N,V_actionMetadata) actionMetadata;
```

## Class methods

```
+[TCSmartAction supportsSecureCoding];
```

## Instance methods

```
-[TCSmartAction actionType];
-[TCSmartAction encodeWithCoder:];
-[TCSmartAction hash];
-[TCSmartAction initWithCoder:];
-[TCSmartAction copyWithZone:];
-[TCSmartAction isEqual:];
-[TCSmartAction actionMetadata];
-[TCSmartAction initWithSmartActionMetadata:];
```
