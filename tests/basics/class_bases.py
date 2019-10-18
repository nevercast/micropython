# test for type.__bases__ implementation

class A:
    pass

class B(object):
    pass

class C(B):
    pass

class D(C, A):
    pass

# Check the attribute exists
print(hasattr(A, '__bases__'))
print(hasattr(B, '__bases__'))
print(hasattr(C, '__bases__'))
print(hasattr(D, '__bases__'))

# Check it is always a tuple
print(type(A.__bases__) == tuple)
print(type(B.__bases__) == tuple)
print(type(C.__bases__) == tuple)
print(type(D.__bases__) == tuple)

# Check size
print(len(A.__bases__) == 1)
print(len(B.__bases__) == 1)
print(len(C.__bases__) == 1)
print(len(D.__bases__) == 2)

# Check values
print(A.__bases__[0] == object)
print(B.__bases__[0] == object)
print(C.__bases__[0] == B)
print(D.__bases__[0] == C)
print(D.__bases__[1] == A)

# Check native bases
native_bases = {
    object: tuple(),
    type(None): (object,),
    bool:
    int:
    str:
    bytes:
    bytearray:
    memoryview:
    float:
    complex:
    tuple:
    list:
    map:
    enumerate:
    filter:
    deque:
    dict:
    ordereddict:
    range:
    set:
    frozenset:
    slice:
    zip:
    array:
    super:
    gen_wrap:

}


# mp_type_bool;
# extern const mp_obj_type_t mp_type_int;
# extern const mp_obj_type_t mp_type_str;
# extern const mp_obj_type_t mp_type_bytes;
# extern const mp_obj_type_t mp_type_bytearray;
# extern const mp_obj_type_t mp_type_memoryview;
# extern const mp_obj_type_t mp_type_float;
# extern const mp_obj_type_t mp_type_complex;
# extern const mp_obj_type_t mp_type_tuple;
# extern const mp_obj_type_t mp_type_list;
# extern const mp_obj_type_t mp_type_map; // map (the python builtin, not the dict implementation detail)
# extern const mp_obj_type_t mp_type_enumerate;
# extern const mp_obj_type_t mp_type_filter;
# extern const mp_obj_type_t mp_type_deque;
# extern const mp_obj_type_t mp_type_dict;
# extern const mp_obj_type_t mp_type_ordereddict;
# extern const mp_obj_type_t mp_type_range;
# extern const mp_obj_type_t mp_type_set;
# extern const mp_obj_type_t mp_type_frozenset;
# extern const mp_obj_type_t mp_type_slice;
# extern const mp_obj_type_t mp_type_zip;
# extern const mp_obj_type_t mp_type_array;
# extern const mp_obj_type_t mp_type_super;
# extern const mp_obj_type_t mp_type_gen_wrap;
# extern const mp_obj_type_t mp_type_native_gen_wrap;
# extern const mp_obj_type_t mp_type_gen_instance;
# extern const mp_obj_type_t mp_type_fun_builtin_0;
# extern const mp_obj_type_t mp_type_fun_builtin_1;
# extern const mp_obj_type_t mp_type_fun_builtin_2;
# extern const mp_obj_type_t mp_type_fun_builtin_3;
# extern const mp_obj_type_t mp_type_fun_builtin_var;
# extern const mp_obj_type_t mp_type_fun_bc;
# extern const mp_obj_type_t mp_type_module;
# extern const mp_obj_type_t mp_type_staticmethod;
# extern const mp_obj_type_t mp_type_classmethod;
# extern const mp_obj_type_t mp_type_property;
# extern const mp_obj_type_t mp_type_stringio;
# extern const mp_obj_type_t mp_type_bytesio;
# extern const mp_obj_type_t mp_type_reversed;
# extern const mp_obj_type_t mp_type_polymorph_iter;

# // Exceptions
# extern const mp_obj_type_t mp_type_BaseException;
# extern const mp_obj_type_t mp_type_ArithmeticError;
# extern const mp_obj_type_t mp_type_AssertionError;
# extern const mp_obj_type_t mp_type_AttributeError;
# extern const mp_obj_type_t mp_type_EOFError;
# extern const mp_obj_type_t mp_type_Exception;
# extern const mp_obj_type_t mp_type_GeneratorExit;
# extern const mp_obj_type_t mp_type_ImportError;
# extern const mp_obj_type_t mp_type_IndentationError;
# extern const mp_obj_type_t mp_type_IndexError;
# extern const mp_obj_type_t mp_type_KeyboardInterrupt;
# extern const mp_obj_type_t mp_type_KeyError;
# extern const mp_obj_type_t mp_type_LookupError;
# extern const mp_obj_type_t mp_type_MemoryError;
# extern const mp_obj_type_t mp_type_NameError;
# extern const mp_obj_type_t mp_type_NotImplementedError;
# extern const mp_obj_type_t mp_type_OSError;
# extern const mp_obj_type_t mp_type_TimeoutError;
# extern const mp_obj_type_t mp_type_OverflowError;
# extern const mp_obj_type_t mp_type_RuntimeError;
# extern const mp_obj_type_t mp_type_StopAsyncIteration;
# extern const mp_obj_type_t mp_type_StopIteration;
# extern const mp_obj_type_t mp_type_SyntaxError;
# extern const mp_obj_type_t mp_type_SystemExit;
# extern const mp_obj_type_t mp_type_TypeError;
# extern const mp_obj_type_t mp_type_UnicodeError;
# extern const mp_obj_type_t mp_type_ValueError;
# extern const mp_obj_type_t mp_type_ViperTypeError;
# extern const mp_obj_type_t mp_type_ZeroDivisionError;