// Generated by gencpp from file semantic_SLAM/deteccion.msg
// DO NOT EDIT!


#ifndef SEMANTIC_SLAM_MESSAGE_DETECCION_H
#define SEMANTIC_SLAM_MESSAGE_DETECCION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace semantic_SLAM
{
template <class ContainerAllocator>
struct deteccion_
{
  typedef deteccion_<ContainerAllocator> Type;

  deteccion_()
    : Class()
    , probability(0.0)
    , xmin(0)
    , ymin(0)
    , xmax(0)
    , ymax(0)
    , depth(0.0)  {
    }
  deteccion_(const ContainerAllocator& _alloc)
    : Class(_alloc)
    , probability(0.0)
    , xmin(0)
    , ymin(0)
    , xmax(0)
    , ymax(0)
    , depth(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _Class_type;
  _Class_type Class;

   typedef double _probability_type;
  _probability_type probability;

   typedef int64_t _xmin_type;
  _xmin_type xmin;

   typedef int64_t _ymin_type;
  _ymin_type ymin;

   typedef int64_t _xmax_type;
  _xmax_type xmax;

   typedef int64_t _ymax_type;
  _ymax_type ymax;

   typedef double _depth_type;
  _depth_type depth;





  typedef boost::shared_ptr< ::semantic_SLAM::deteccion_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::semantic_SLAM::deteccion_<ContainerAllocator> const> ConstPtr;

}; // struct deteccion_

typedef ::semantic_SLAM::deteccion_<std::allocator<void> > deteccion;

typedef boost::shared_ptr< ::semantic_SLAM::deteccion > deteccionPtr;
typedef boost::shared_ptr< ::semantic_SLAM::deteccion const> deteccionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::semantic_SLAM::deteccion_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::semantic_SLAM::deteccion_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::semantic_SLAM::deteccion_<ContainerAllocator1> & lhs, const ::semantic_SLAM::deteccion_<ContainerAllocator2> & rhs)
{
  return lhs.Class == rhs.Class &&
    lhs.probability == rhs.probability &&
    lhs.xmin == rhs.xmin &&
    lhs.ymin == rhs.ymin &&
    lhs.xmax == rhs.xmax &&
    lhs.ymax == rhs.ymax &&
    lhs.depth == rhs.depth;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::semantic_SLAM::deteccion_<ContainerAllocator1> & lhs, const ::semantic_SLAM::deteccion_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace semantic_SLAM

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::semantic_SLAM::deteccion_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::semantic_SLAM::deteccion_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::semantic_SLAM::deteccion_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::semantic_SLAM::deteccion_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::semantic_SLAM::deteccion_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::semantic_SLAM::deteccion_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::semantic_SLAM::deteccion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "736162dbf88cd926f35ced1ad47b7fa7";
  }

  static const char* value(const ::semantic_SLAM::deteccion_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x736162dbf88cd926ULL;
  static const uint64_t static_value2 = 0xf35ced1ad47b7fa7ULL;
};

template<class ContainerAllocator>
struct DataType< ::semantic_SLAM::deteccion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "semantic_SLAM/deteccion";
  }

  static const char* value(const ::semantic_SLAM::deteccion_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::semantic_SLAM::deteccion_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string Class\n"
"float64 probability\n"
"int64 xmin\n"
"int64 ymin\n"
"int64 xmax\n"
"int64 ymax\n"
"float64 depth\n"
"\n"
;
  }

  static const char* value(const ::semantic_SLAM::deteccion_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::semantic_SLAM::deteccion_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.Class);
      stream.next(m.probability);
      stream.next(m.xmin);
      stream.next(m.ymin);
      stream.next(m.xmax);
      stream.next(m.ymax);
      stream.next(m.depth);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct deteccion_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::semantic_SLAM::deteccion_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::semantic_SLAM::deteccion_<ContainerAllocator>& v)
  {
    s << indent << "Class: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.Class);
    s << indent << "probability: ";
    Printer<double>::stream(s, indent + "  ", v.probability);
    s << indent << "xmin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmin);
    s << indent << "ymin: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymin);
    s << indent << "xmax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.xmax);
    s << indent << "ymax: ";
    Printer<int64_t>::stream(s, indent + "  ", v.ymax);
    s << indent << "depth: ";
    Printer<double>::stream(s, indent + "  ", v.depth);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SEMANTIC_SLAM_MESSAGE_DETECCION_H
