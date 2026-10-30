# `NIBTCSRangingConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _identifier;
@"NSString" _requestingAppBundleIdentifier;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_identifier) identifier;
@property (T@"NSString",C,N,V_requestingAppBundleIdentifier) requestingAppBundleIdentifier;
```

## Class methods

```
+[NIBTCSRangingConfiguration supportsSecureCoding];
```

## Instance methods

```
-[NIBTCSRangingConfiguration identifier];
-[NIBTCSRangingConfiguration descriptionInternal];
-[NIBTCSRangingConfiguration encodeWithCoder:];
-[NIBTCSRangingConfiguration hash];
-[NIBTCSRangingConfiguration description];
-[NIBTCSRangingConfiguration initWithCoder:];
-[NIBTCSRangingConfiguration copyWithZone:];
-[NIBTCSRangingConfiguration isEqual:];
-[NIBTCSRangingConfiguration initWithIdentifier:];
-[NIBTCSRangingConfiguration requestingAppBundleIdentifier];
-[NIBTCSRangingConfiguration setRequestingAppBundleIdentifier:];
```
