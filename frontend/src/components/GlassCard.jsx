import { motion } from 'framer-motion';
export default function GlassCard({children}){
 return (
  <motion.div initial={{opacity:0,y:20}} animate={{opacity:1,y:0}} className="w-full max-w-md bg-white/20 backdrop-blur-xl p-6 rounded-3xl shadow-xl border border-white/30">
    {children}
  </motion.div>
 );
}
