# `ETModelDef`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 21 instance methods, 0 class methods

## Instance variables

```
{map<std::string, std::vector<std::string>, std::less<std::string>, std::allocator<std::pair<const std::string, std::vector<std::string>>>>="__tree_"{__tree<std::__value_type<std::string, std::vector<std::string>>, std::__map_value_compare<std::string, std::pair<const std::string, std::vector<std::string>>, std::less<std::string>>, std::allocator<std::pair<const std::string, std::vector<std::string>>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} layer_variable_names;
@"NSMutableArray" _all_variables;
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _network;
{shared_ptr<Espresso::gradient_builder>="__ptr_"^{gradient_builder}"__cntrl_"^{__shared_weak_count}} _gb;
```

## Properties

```
@property (T{shared_ptr<Espresso::net>=^{net}^{__shared_weak_count}},V_network) network;
@property (T@"NSMutableArray",&,V_all_variables) all_variables;
@property (T{shared_ptr<Espresso::gradient_builder>=^{gradient_builder}^{__shared_weak_count}},V_gb) gb;
```

## Instance methods

```
-[ETModelDef network];
-[ETModelDef variables];
-[ETModelDef initWithNetwork:];
-[ETModelDef layerNames];
-[ETModelDef biasesForLayer:];
-[ETModelDef updateLayer:withWeights:length:];
-[ETModelDef all_variables];
-[ETModelDef configureLayersToTrain:reinitializeVariables:];
-[ETModelDef gb];
-[ETModelDef layerForName:];
-[ETModelDef randomizeWeightsForLayer:withSeed:];
-[ETModelDef setAll_variables:];
-[ETModelDef setGb:];
-[ETModelDef setNetwork:];
-[ETModelDef setupVariablesDef];
-[ETModelDef topNamesForLayerIndex:];
-[ETModelDef transformForTraining:];
-[ETModelDef updateLayer:withBiases:length:];
-[ETModelDef variableForLayer:kind:];
-[ETModelDef variableNameForLayer:kind:];
-[ETModelDef weightsForLayer:];
```
