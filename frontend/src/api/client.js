import axios from "axios";

const ORDER_API = import.meta.env.VITE_ORDER_API || "/api/orders";

const DRIVER_API = import.meta.env.VITE_DRIVER_API || "/api/drivers";


const ordersApi = axios.create({
  baseURL: ORDER_API,
  headers: { "Content-Type": "application/json" },
});

const driversApi = axios.create({
  baseURL: DRIVER_API,
  headers: { "Content-Type": "application/json" },
});
// Orders
export const createOrder = (data) => ordersApi.post('/', data)
export const getOrders = () => ordersApi.get('/')
export const optimizeRoutes = () => ordersApi.post('/optimize')
export const getUnassignedOrders = () => ordersApi.get('/unassigned')
export const getDriverOrders = (driverId) => ordersApi.get(`/driver/${driverId}`)
export const getDriverRouteGeometry = (driverId) => ordersApi.get(`/driver/${driverId}/route-geometry`)
export const markOrderDelivered = (orderId) => ordersApi.patch(`/${orderId}/deliver`)

// Drivers
export const createDriver = (data) => driversApi.post('/', data)
export const getDrivers = () => driversApi.get('/')
export const getDriverByPhone = (phone) => driversApi.get(`/login?phone=${encodeURIComponent(phone)}`)

export default { ordersApi, driversApi }
