import { Room } from './rooms';

export const ROOMS: Room[] = [
    {   id: 1,
        komnaty: [
            {
                photo: 'https://blog.ostrovok.ru/wp-content/uploads/2012/02/download.jpg',
                description: "Nice",
                price: 50000,
                chel: 4,
                zanyat: true,
            },
            {
                photo: 'https://blog.kupibilet.ru/wp-content/uploads/2014/03/Castlerosse-Hotel-and-Holiday-Homes-Clean-Family-Room-Killarney-IE_b-1280x720.jpg',
                description: "Nice",
                price: 50000,
                chel: 5,
                zanyat: false,
            }
        ]
    },
    {   id: 2,
        komnaty: [{
            photo: 'https://blog.kupibilet.ru/wp-content/uploads/2014/03/Castlerosse-Hotel-and-Holiday-Homes-Clean-Family-Room-Killarney-IE_b-1280x720.jpg',
            description: "Nice",
            price: 50000,
            chel: 5,
            zanyat: false,
        }]
        
    },
    {   id: 3,
        komnaty: [{
            photo: 'https://lh3.googleusercontent.com/proxy/qkFyBUutzqknY8Wre04P_60tCAnbEltu-9bCziu7c11eryB_n8kykxfdd7BUdDFCGIdSUW70RBVqSgbguKMiK7WyZVWwM0jOfsbt6gnuwHGUJMT6t5v9',
            description: "Nice",
            price: 50000,
            chel: 1,
            zanyat: false,
        }]
        
    },
]