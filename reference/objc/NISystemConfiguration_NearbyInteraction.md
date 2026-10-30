# `NISystemConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
B _prewarmUWB;
B _prewarmSecureElementChannel;
```

## Properties

```
@property (TB,N,V_prewarmUWB) prewarmUWB;
@property (TB,N,V_prewarmSecureElementChannel) prewarmSecureElementChannel;
```

## Class methods

```
+[NISystemConfiguration supportsSecureCoding];
+[NISystemConfiguration new];
```

## Instance methods

```
-[NISystemConfiguration init];
-[NISystemConfiguration descriptionInternal];
-[NISystemConfiguration encodeWithCoder:];
-[NISystemConfiguration hash];
-[NISystemConfiguration description];
-[NISystemConfiguration initWithCoder:];
-[NISystemConfiguration copyWithZone:];
-[NISystemConfiguration isEqual:];
-[NISystemConfiguration setPrewarmSecureElementChannel:];
-[NISystemConfiguration _internalIsMemoryAssertionRequired];
-[NISystemConfiguration prewarmSecureElementChannel];
-[NISystemConfiguration prewarmUWB];
-[NISystemConfiguration setPrewarmUWB:];
```
