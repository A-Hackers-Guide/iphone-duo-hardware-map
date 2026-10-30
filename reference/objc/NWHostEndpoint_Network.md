# `NWHostEndpoint`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWEndpoint`
- 0 instance variables, 2 properties, 3 instance methods, 2 class methods

## Properties

```
@property (T@"NSString",R,N) hostname;
@property (T@"NSString",R,N) port;
```

## Class methods

```
+[NWHostEndpoint endpointType];
+[NWHostEndpoint endpointWithHostname:port:];
```

## Instance methods

```
-[NWHostEndpoint hostname];
-[NWHostEndpoint descriptionWithIndent:showFullContent:];
-[NWHostEndpoint port];
```
