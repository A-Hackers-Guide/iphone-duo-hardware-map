# `BWNodeConfigurationLiveMessage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNodeMessage`
- 2 instance variables, 2 properties, 3 instance methods, 2 class methods

## Instance variables

```
q _configurationID;
@"BWFormat" _updatedFormat;
```

## Properties

```
@property (Tq,R) configurationID;
@property (T@"BWFormat",R) updatedFormat;
```

## Class methods

```
+[BWNodeConfigurationLiveMessage newMessageWithConfigurationID:];
+[BWNodeConfigurationLiveMessage newMessageWithConfigurationID:updatedFormat:];
```

## Instance methods

```
-[BWNodeConfigurationLiveMessage configurationID];
-[BWNodeConfigurationLiveMessage dealloc];
-[BWNodeConfigurationLiveMessage updatedFormat];
```
