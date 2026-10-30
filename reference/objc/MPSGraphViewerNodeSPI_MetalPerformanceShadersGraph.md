# `MPSGraphViewerNodeSPI`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 7 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" _type;
@"NSArray" _inputs;
@"NSArray" _outputs;
@"NSArray" _properties;
@"NSArray" _regions;
@"NSString" _localizedDescription;
@"NSString" _location;
```

## Properties

```
@property (T@"NSString",R,N,V_type) type;
@property (T@"NSArray",R,N,V_inputs) inputs;
@property (T@"NSArray",R,N,V_outputs) outputs;
@property (T@"NSArray",R,N,V_properties) properties;
@property (T@"NSArray",R,N,V_regions) regions;
@property (T@"NSString",&,N,V_localizedDescription) localizedDescription;
@property (T@"NSString",&,N,V_location) location;
```

## Instance methods

```
-[MPSGraphViewerNodeSPI outputs];
-[MPSGraphViewerNodeSPI regions];
-[MPSGraphViewerNodeSPI properties];
-[MPSGraphViewerNodeSPI localizedDescription];
-[MPSGraphViewerNodeSPI inputs];
-[MPSGraphViewerNodeSPI location];
-[MPSGraphViewerNodeSPI jsonDictionary];
-[MPSGraphViewerNodeSPI type];
-[MPSGraphViewerNodeSPI setLocation:];
-[MPSGraphViewerNodeSPI setLocalizedDescription:];
-[MPSGraphViewerNodeSPI initWithJSONDictionary:];
-[MPSGraphViewerNodeSPI initWithType:inputs:outputs:properties:regions:];
```
