# `NWBrowseDescriptor`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWPrettyDescription`
- 1 instance variables, 4 properties, 13 instance methods, 5 class methods

## Instance variables

```
@"NSObject<OS_nw_browse_descriptor>" _internalDescriptor;
```

## Properties

```
@property (T@"NSObject<OS_nw_browse_descriptor>",&,N,V_internalDescriptor) internalDescriptor;
@property (T@"NSString",R,C,N) privateDescription;
@property (T@"NSString",R,N) bonjourServiceDomain;
@property (T@"NSString",R,N) bonjourServiceType;
```

## Class methods

```
+[NWBrowseDescriptor copyClassForDescriptorType:];
+[NWBrowseDescriptor descriptorType];
+[NWBrowseDescriptor descriptorWithInternalDescriptor:];
+[NWBrowseDescriptor descriptorWithProtocolBufferData:];
+[NWBrowseDescriptor supportsBrowseCallback];
```

## Instance methods

```
-[NWBrowseDescriptor createProtocolBufferObject];
-[NWBrowseDescriptor initWithDescriptor:];
-[NWBrowseDescriptor encodedData];
-[NWBrowseDescriptor privateDescription];
-[NWBrowseDescriptor descriptionWithIndent:showFullContent:];
-[NWBrowseDescriptor bonjourServiceType];
-[NWBrowseDescriptor description];
-[NWBrowseDescriptor copyWithZone:];
-[NWBrowseDescriptor bonjourServiceDomain];
-[NWBrowseDescriptor browseWithCompletionHandler:];
-[NWBrowseDescriptor initWithEncodedData:];
-[NWBrowseDescriptor internalDescriptor];
-[NWBrowseDescriptor setInternalDescriptor:];
```
