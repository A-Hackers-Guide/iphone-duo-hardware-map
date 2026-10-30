# `NWBonjourServiceEndpoint`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWEndpoint`
- 0 instance variables, 3 properties, 4 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) type;
@property (T@"NSString",R,N) domain;
```

## Class methods

```
+[NWBonjourServiceEndpoint endpointType];
+[NWBonjourServiceEndpoint endpointWithName:type:domain:];
```

## Instance methods

```
-[NWBonjourServiceEndpoint domain];
-[NWBonjourServiceEndpoint descriptionWithIndent:showFullContent:];
-[NWBonjourServiceEndpoint type];
-[NWBonjourServiceEndpoint name];
```
